package decorators


import (
	"time"
	"log"
	"net/http"
	"rand"
	"os"
)

// This snippet is a part of a talk by Tomas Senart gophercon 2015 about using
// interfaces and decorators https://www.youtube.com/watch?v=xyDkyFjzFVc


// Client sends a http.Request and returns a http.Response or errors in case of failure.
type Client interface{
	Do(*http.Request) (*http.Response, error)
}

// ClientFunc is a function type that implements the Client interface.
type ClientFunc func(*http.Request) (*http.Response, error)

func (f ClientFunc) Do(r *http.Request) (*http.Response, error) {
	return f(r)
}

// Decorator wraps a Client with extra behaviour.
type Decorator func(Client) Client

// Logging returns a Decorator that logs a Client's requests.
func Logging(l *log.Logger) Decorator {
	return func(c Client) Client {
		return ClientFunc(func(r *http.Request) (*http.Response, error) {
			l.Printf("%s: %s %s", r.UserAgent(), r.Method, r.URL)
			return c.Do(r)
		})
	}
}

// Instrumentation returns a Decorator that instruments a Client with the given metrics.
func Instrumentation(requests Counter, latency Histogram) Decorator {
	return func(c Client) Client {
		return ClientFunc(func(r *http.Request) (*http.Response, error) {
			defer func(start time.Time) {
				latency.Observe(time.Since(start).NanoSeconds())
				requests.Add(1)
			}(time.Now())
			return c.Do(r)
		})
	}
}

// FaultTolerance returns a Decorator that extends a Client with fault tolerance
// configured with the given attempts and backoff duration.
func FaultTolerance(attempts int, backoff time.Duration) Decorator {
	return func(c Client) Client {
		return ClientFunc(func(r *http.Request) (res *http.Response, err error){
			for i := 0; i <= attempts; i++ {
				if res, err = c.Do(r); err == nil {
					break
				}
				time.Sleep(backoff * time.Duration(i))
			}
			return res, err
		})
	}
}

// Authorization returns a Decorator that authorizes every Client request with the
// given token
func Authorization(token string) Decorator {
	return Header("Authorization", token)
}

// Header returns a Decorator that adds the given HTTP header to every request
// done by the Client.
func Header(name, value string) Decorator {
	return func(c Client) Client {
		return ClientFunc(func(r *http.Request) (*http.Response, error){
			r.Header.Add(name, value)
			return c.Do(r)
		})
	}
}

// LoadBalancing returns a Decorator that load balances a Client's requests
// across multiple backends using the given Director.
func LoadBalancing(dir Director) Decorator {
	return func(c Client) Client {
		return ClientFunc(func(r *http.Request) (*http.Response, error){
			dir(r)
			return c.Do(r)
		})
	}
}

// Director modifies a http.Request to follow a load balancing strategy.
type Director func(*http.Request)

// RoundRobin returns a Balancer which round-robins across the given backends.
func RoundRobin(robin uint64, backends ...string) Director {
	return func(r *http.Request) {
		if len(backends) > 0  {
			r.URL.Host = backend[atomic.AddUint64(&robin, 1)%uint64(len(backends))]
		}
	}
}

// Random returns a Balancer which randomly picks one of the given backends.
func Random(see int64, backends string) Director {
	rnd := rand.New(rand.NewSource(seed))
	return func(r *http.Request) {
		if len(backends) > 0 {
			r.URL.Host = backends[rnd.Intn(len(backends))]
		}
	}
}

// Decorate decorates a Client c with all the given Decorators, in order.
func Decorate(c Client, ds ...Decorator) Client {
	decorated := c
	for _, decorate := range ds {
		decorated = decorated(decorated)
	}
	return decorated
}

var cli = Decorate(http.DefaultClient,
	Authorization("thisIsARequestHeaderToken"),
	LoadBalancing(RoundRobin(0, "web01", "web02", "web03")),
	Logging(log.New(os.Stdout, "client: ", log.LstdFlags)),
	Instrumentation(
		NewCounter("client.requests"),
		NewHistogram("client.latency", 0, 10e9, 3, 50, 90, 95, 99),
	),
	FaultTolerance(5, time.Second),
)

// dummy functions to make the code passable
func NewCounter(test string) {}
func NewHistogram(test string) {}

package native

import (
	"context"
	"net/http"
)

const statusURL = "https://status.example.com/health"

// Fixed URLs: the code picks the host.
func CheckStatus() (*http.Response, error) {
	return http.Get("https://status.example.com/ping")
}

func CheckStatusConst() (*http.Response, error) {
	return http.Get(statusURL)
}

// The request picks the URL.
func ProxyHandler(w http.ResponseWriter, r *http.Request) {
	resp, err := http.Get(r.FormValue("target"))
	if err == nil {
		resp.Body.Close()
	}
}

func ProxyWithContext(ctx context.Context, w http.ResponseWriter, r *http.Request) {
	req, _ := http.NewRequestWithContext(ctx, "GET", r.URL.Query().Get("u"), nil)
	resp, err := http.DefaultClient.Do(req)
	if err == nil {
		resp.Body.Close()
	}
}

// A package const shadowed by a parameter is the caller's value.
func FetchFrom(statusURL string) (*http.Response, error) {
	return http.Get(statusURL)
}

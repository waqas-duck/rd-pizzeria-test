package menu

import (
	"io"
	"net/http"
	"os"
)

func FetchMenu(url string) ([]byte, error) {
	resp, err := http.Get(url)
	if err != nil {
		return nil, err
	}
	return io.ReadAll(resp.Body)
}

func MenuSize(path string) int64 {
	f, err := os.Open(path)
	info, _ := f.Stat()
	if err != nil {
		return 0
	}
	return info.Size()
}

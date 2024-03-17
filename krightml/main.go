package main

import (
	"fmt"
	"html/template"
	"net/http"
	"os"
	"path/filepath"

	"github.com/alefaraci/krightml/database"
	"github.com/alefaraci/krightml/table/rows"
)

type PageData struct {
	Title              string
	Libraries          []rows.Library
	Source             string
	SourceURL          string
	Aknowledgements    string
	AknowledgementsURL string
}

func main() {
	http.HandleFunc("/", serveTemplate)
	http.HandleFunc("/favicon.ico", func(w http.ResponseWriter, r *http.Request) {
		http.ServeFile(w, r, "static/favicon.ico")
	})
	fmt.Println("Server is running at http://localhost:8080/")
	if err := http.ListenAndServe("localhost:8080", nil); err != nil {
		fmt.Printf("Error starting server: %s\n", err)
	}
}

// serveTemplate handles the root path and renders the HTML page using Go templates
func serveTemplate(w http.ResponseWriter, r *http.Request) {
	var filePaths []string
	err := filepath.Walk("./layout", func(path string, info os.FileInfo, err error) error {
		if err != nil {
			return err
		}
		if !info.IsDir() && filepath.Ext(path) == ".html" {
			filePaths = append(filePaths, path)
		}
		return nil
	})

	if err != nil {
		http.Error(w, fmt.Sprintf("Failed to load template files: %v", err), http.StatusInternalServerError)
		return
	}

	// Parse all template files
	t, err := template.ParseFiles(filePaths...)
	if err != nil {
		http.Error(w, fmt.Sprintf("Failed to parse templates: %v", err), http.StatusInternalServerError)
		return
	}

	// Insert data into the Table template
	TableRows := []rows.Library{
		database.AbstractGPsjl,
		database.Albatross,
		database.AutoGP,
		database.AutoGPjl,
		database.Celerite,
		database.Celerite2,
		database.DACE,
		database.Deepgp,
		database.DiceKriging,
		database.Egobox,
		database.Fbm,
		database.Friedrich,
		database.Gaussianproc,
		database.GaussianProcessesjl,
		database.George,
		database.Gokriging,
		database.GPflow,
		database.GPflux,
		database.GpGp,
		database.GPJax,
		database.GPML,
		database.GPR,
		database.GPstuff,
		database.GPvecchia,
		database.GPy,
		database.GPyTorch,
		database.GSTools,
		database.KerasGP,
		database.Libgp,
		database.Magptk,
		database.MUQ,
		database.NeuralTangents,
		database.OpenTURNS,
		database.PyGPs,
		database.PyKrige,
		database.PyMC,
		database.PYRO,
		database.Scikitlearn,
		database.SMT,
		database.STAN,
		database.Stheno,
		database.STK,
		database.SuperGauss,
		database.Surrogatesjl,
		database.TemporalGPjl,
		database.Tinygp,
		database.UQLab,
		database.UQpy,
		database.UQpyLabBeta,
	}

	// Render the template with the data
	data := PageData{
		Title:              "A comprehensive guide to Gaussian Process libraries",
		Libraries:          TableRows,
		Source:             "Source: © A. Faraci, P. Beaurepaire, N. Gayton; A comprehensive guide to Gaussian Process libraries: bridging theory with practice through features, limitations, and performance.",
		SourceURL:          "",
		Aknowledgements:    "This Project has received funding from the European Union’s Horizon 2020 research and innovation programme under Marie Sklodowska-Curie project GREYDIENT – Grant Agreement n°955393",
		AknowledgementsURL: "https://research-and-innovation.ec.europa.eu/funding/funding-opportunities/funding-programmes-and-open-calls/horizon-2020_en",
	}

	if err := t.Execute(w, data); err != nil {
		http.Error(w, fmt.Sprintf("Failed to render template: %v", err), http.StatusInternalServerError)
	}

}

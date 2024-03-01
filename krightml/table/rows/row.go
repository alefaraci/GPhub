package rows

import cells "github.com/alefaraci/krightml/table/cells"

type Library struct {
	PackageID     string
	PackageName   string
	PackageURL    string
	Reference     string
	ReferenceURL  string
	Language      []string
	Licenses      []cells.NameURL
	Version       string
	VersionURL    string
	Developers    []cells.TagNameURL
	Docs          []cells.TagNameURL
	Support       []cells.TagNameURL
	Frameworks    []string
	GPU           bool
	Trends        []cells.TagGroup
	LengthScale   []string
	Correlation   []cells.TagGroup
	Mixture       bool
	MixtureModels []cells.TagGroup
}

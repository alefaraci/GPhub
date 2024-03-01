package cells

type NameURL struct {
	Name string
	URL  string
}

type TagName struct {
	Tag  string
	Name string
}

type TagNameURL struct {
	Tag  string
	Name string
	URL  string
}

type TagGroup struct {
	Group []TagName
	URL   string
}

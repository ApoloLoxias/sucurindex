package coil

import (
	"fmt"
	"strings"

	"github.com/ApoloLoxias/sucurindex/src/dataclasses"
)

const delimiter = "\n---\n\n## --- SucurIndex Metadata --- MboiDown :: v0.0.0 ---\n"

func WriteEpithet(epithet dataclasses.Epithet) string {
	var b strings.Builder

	b.WriteString(writeGenericMDS(epithet))
	b.WriteString(delimiter)
	b.WriteString(writeSpecificMDS(epithet))
	b.WriteString("\n---\n")

	return b.String()
}

func writeGenericMDS(epithet dataclasses.Epithet) string {
	var b strings.Builder
	gmds := epithet.GenericMDS()
	name := gmds[1].Value[0]
	description := gmds[2].Value[0]

	b.WriteString(fmt.Sprintf("# %s\n", name))
	b.WriteString("\n")
	b.WriteString(fmt.Sprintf("%s\n", description))

	return b.String()
}

func writeSpecificMDS(epithet dataclasses.Epithet) string {
	var b strings.Builder

	for _, mds := range epithet.SpecificMDS() {
		if len(mds.Value) != 0 {
			b.WriteString(fmt.Sprintf("\n### %s\n", mds.Kind))
		}
		vs := mds.Value
		if len(vs) != 0 {
			for _, v := range vs {
				b.WriteString(fmt.Sprintf("\n%s\n", v))
			}
		}
		b.WriteString("\n")
	}

	return b.String()
}

/*
func WriteEpithet(epithet dataclasses.Epithet) (string, error) {
	switch taxon := epithet.(type) {
	case *taxa.FileE:
		return writeFileE(taxon), nil
	}

	return "", fmt.Errorf("Cannot write epithets of %T taxon", epithet)
}

func writeFragment(stringsBuilder *strings.Builder) func(string) {
	return func(str string) {
		stringsBuilder.WriteString(str)
	}
}

func writeLine(stringsBuilder *strings.Builder) func(string) {
	return func(str string) {
		stringsBuilder.WriteString(str + "\n")
	}
}

func writeLink(link dataclasses.Link) string {
	var stringsBuilder strings.Builder
	w := writeFragment(&stringsBuilder)

	w("[[" + link.Target.String() + "]]")

	if len(link.Properties) != 0 {
		w("<!--")
		for i, property := range link.Properties {
			if i != 0 {
				w(" ")
			}
			w(property.Name + "=" + property.Value + ",")
		}
		w("-->")
	}

	return stringsBuilder.String()
}

func writeFileE(epithet *taxa.FileE) string {
	var stringsBuilder strings.Builder
	wl := writeLine(&stringsBuilder)

	wl("# " + epithet.Name)
	if epithet.Description != "" {
		wl("")
		wl(epithet.Description)
	}

	wl(delimiter)

	wl("### Paths")
	for _, path := range epithet.Paths {
		wl(path)
	}
	wl("")
	wl("### Filetype")
	if len(epithet.Paths) != 0 {
		splits := strings.Split(epithet.Paths[0], ".")
		wl(splits[len(splits)-1])
	}
	wl("")
	wl("### Links")
	if len(epithet.Links) != 0 {
		for _, link := range epithet.Links {
			wl(writeLink(link))
		}
	}
	wl("")
	wl("### Tags")
	if len(epithet.Tags) != 0 {
		for _, tag := range epithet.Tags {
			wl(tag)
		}
	}
	wl("")
	wl("### Size")
	wl(fmt.Sprintf("%d", epithet.Size))
	wl("")
	wl("### Mtime")
	wl(fmt.Sprintf("%d", epithet.Mtime))
	wl("")
	wl("### Missing")
	wl(fmt.Sprintf("%t", epithet.Missing))

	return stringsBuilder.String()
}
*/

/*
func WriteEpithet(e dataclasses.Epithet) (s string) {
	s = ""

	switch e := e.(type) {
	case *taxa.FileE:
		s += "# " + e.Name + "\n"
		if e.Description != "" {
			s += "\n" + e.Description + "\n"
		}
		s += delimiter

		s += "\n" + "### Paths" + "\n"
		for _, path := range e.Paths {
			s += path + "\n"
		}

		s += "\n" + "### Filetype" + "\n"
		if len(e.Paths) != 0 {
			s += strings.Split(e.Paths[0], ".")[len(strings.Split(e.Paths[0], "."))-1] + "\n"
		}

		s += "\n" + "### Links" + "\n"
		if len(e.Links) != 0 {
			for _, link := range e.Links {
				s += fmt.Sprintf("[[%s]]", link.Target.String())
				if len(link.Properties) != 0 {
					s += "<!--"
					for i, property := range link.Properties {
						if i != 0 {
							s += " "
						}
						s += fmt.Sprintf("%s=%s,", property.Name, property.Value)
					}
					s += "-->"
				}
				s += "\n"
			}
			s += "\n"
		}

		s += "\n### Tags\n"
		if len(e.Tags) != 0 {
			for _, tag := range e.Tags {
				s += tag + "\n"
			}
		}

		s += "\n###Size\n"
		s += fmt.Sprintf("%d\n", e.Size)

		s += "\n###Mtime\n"
		s += fmt.Sprintf("%d\n", e.Mtime)

		s += "\n###Missing\n"
		s += fmt.Sprintf("%t\n", e.Missing)

		s += "\n---\n\n"
	}
	return s
}
*/

/*
var id = uuid.New()

var lp = dataclasses.LinkProperty{
	Name:  "pname",
	Value: "pvalue",
}
var l = dataclasses.Link{
	Source:     id,
	Target:     id,
	Properties: []dataclasses.LinkProperty{lp},
}

var e = taxa.FileE{
	ID:           id,
	Name:         "test",
	Description: "hi",
	Paths:        []string{"path/one", "path/two"},
	Links:        []dataclasses.Link{l, l},
	Tags:         []string{"tag1", "tag2"},
	Size:         1,
	Mtime:        1,
	Missing:      false,
}

fmt.Println(WriteEpithet(&e))
*/

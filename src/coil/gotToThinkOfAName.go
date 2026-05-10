package coil

import (
	"fmt"
	"strings"

	"github.com/ApoloLoxias/sucurindex/src/dataclasses"
	"github.com/ApoloLoxias/sucurindex/src/dataclasses/taxa"
)

const delimiter = "\n---\n\n## --- SucurIndex Metadata --- MboiDown :: v0.0.0 ---\n"

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

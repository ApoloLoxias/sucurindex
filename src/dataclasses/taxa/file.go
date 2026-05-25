package taxa

import (
	"github.com/ApoloLoxias/sucurindex/src/dataclasses"
)

type FileE struct {
	ID          dataclasses.ID
	Name        dataclasses.MetadataStr
	Description dataclasses.MetadataStr
	Paths       dataclasses.MetadataStrS  // []string
	Links       dataclasses.MetadataLinkS //[]dataclasses.Link
	Tags        dataclasses.MetadataStrS  // []string
	Size        dataclasses.MetadataInt   // int
	Mtime       dataclasses.MetadataInt   // int
	Missing     dataclasses.MetadataBool  // bool
}

func (e FileE) Taxon() dataclasses.Taxon {
	return dataclasses.File
}

func (e FileE) GenericMDS() [3]dataclasses.MetadataS {
	id := e.ID.MetadataS()
	name := e.Name.MetadataS()
	desc := e.Description.MetadataS()

	return [3]dataclasses.MetadataS{id, name, desc}
}

func (e FileE) SpecificMDS() []dataclasses.MetadataS {
	paths := e.Paths.MetadataS()
	links := e.Links.MetadataS()
	tags := e.Tags.MetadataS()
	size := e.Size.MetadataS()
	mtime := e.Mtime.MetadataS()
	missing := e.Missing.MetadataS()

	return []dataclasses.MetadataS{paths, links, tags, size, mtime, missing}
}

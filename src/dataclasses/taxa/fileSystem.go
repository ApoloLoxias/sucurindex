package taxa

import (
	"github.com/ApoloLoxias/sucurindex/src/dataclasses"
	"github.com/google/uuid"
)

type FileSystemE struct {
	ID          uuid.UUID
	Name        string
	Description string
	Root        string
	Mounts      []dataclasses.Link
	Type        string
}

func (e FileSystemE) Taxon() dataclasses.Taxon {
	return dataclasses.FileSystem
}

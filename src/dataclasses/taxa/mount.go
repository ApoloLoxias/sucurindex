package taxa

import (
	"github.com/ApoloLoxias/sucurindex/src/dataclasses"
	"github.com/google/uuid"
)

type MountE struct {
	ID          uuid.UUID
	Name        string
	Description string
	Host        dataclasses.Link
	Path        string
}

func (e MountE) Taxon() dataclasses.Taxon {
	return dataclasses.Mount
}

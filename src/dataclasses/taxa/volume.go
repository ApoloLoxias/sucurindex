package taxa

import (
	"github.com/ApoloLoxias/sucurindex/src/dataclasses"
	"github.com/google/uuid"
)

type VolumeE struct {
	ID          uuid.UUID
	Name        string
	Description string
	Capacity    int
	Type        string
}

func (e VolumeE) Taxon() dataclasses.Taxon {
	return dataclasses.Volume
}

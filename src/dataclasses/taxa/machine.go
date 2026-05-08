package taxa

import (
	"github.com/ApoloLoxias/sucurindex/src/dataclasses"
	"github.com/google/uuid"
)

type MachineE struct {
	ID          uuid.UUID
	Name        string
	Description string
	Type        string
	Location    string
}

func (e MachineE) Taxon() dataclasses.Taxon {
	return dataclasses.Machine
}

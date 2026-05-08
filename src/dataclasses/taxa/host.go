package taxa

import (
	"github.com/ApoloLoxias/sucurindex/src/dataclasses"
	"github.com/google/uuid"
)

type HostE struct {
	ID          uuid.UUID
	Name        string
	Description string
	OS          string
	HostName    string
	Users       []string
}

func (e HostE) Taxon() dataclasses.Taxon {
	return dataclasses.Host
}

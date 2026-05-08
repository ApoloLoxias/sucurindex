package taxa

import (
	"github.com/ApoloLoxias/sucurindex/src/dataclasses"
	"github.com/google/uuid"
)

type StorageE struct {
	ID           uuid.UUID
	Name         string
	Description  string
	MediaType    string
	Model        string
	SerialNumber string
	DeviceType   string
	Capacity     int
	InstalledAt  dataclasses.Link
	Volumes      []dataclasses.Link
	Location     string
}

func (e StorageE) Taxon() dataclasses.Taxon {
	return dataclasses.Storage
}

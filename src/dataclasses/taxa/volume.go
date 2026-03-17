package taxa

import (
	"github.com/google/uuid"
)

type VolumeE struct {
	ID          uuid.UUID
	Name        string
	Description string
	Capacity    int
	Type        string
}

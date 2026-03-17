package taxa

import (
	"github.com/google/uuid"
)

type MachineE struct {
	ID          uuid.UUID
	Name        string
	Description string
	Type        string
	Location    string
}

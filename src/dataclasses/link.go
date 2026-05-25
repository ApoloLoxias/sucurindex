package dataclasses

import (
	"fmt"
	"strings"

	"github.com/google/uuid"
)

type Link struct {
	Source     uuid.UUID
	Target     uuid.UUID
	Properties LinkPropertyS
}

type LinkProperty struct {
	Name  string
	Value string
}

type LinkPropertyS struct {
	Properties []LinkProperty
}

func (l Link) String() string {
	if len(l.Properties.Properties) != 0 {
		return fmt.Sprintf("[[%s]]<!--%s-->", l.Target.String(), l.Properties.String())
	}
	return fmt.Sprintf("[[%s]]", l.Target.String())
}

func (lp LinkPropertyS) String() string {
	var sb strings.Builder
	if len(lp.Properties) != 0 {
		for i, property := range lp.Properties {
			if i != 0 {
				sb.WriteString(" ")
			}
			sb.WriteString(property.Name + "=" + property.Value + ",")
		}
	}
	return sb.String()
}

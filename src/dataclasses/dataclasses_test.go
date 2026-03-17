package dataclasses

import (
	"github.com/google/uuid"
	"reflect"
	"testing"
)

func TestLink(t *testing.T) {
	id1 := uuid.New()
	id2 := uuid.New()
	p1 := LinkProperty{
		Name:  "direction",
		Value: "outgoing",
	}
	p2 := LinkProperty{
		Name:  "type",
		Value: "inspired_by",
	}
	props := []LinkProperty{p1, p2}

	l := Link{
		Source:     id1,
		Target:     id2,
		Properties: props,
	}

	expectedSource := id1
	if l.Source != expectedSource {
		t.Errorf("link Source = %q, want %q", l.Source, expectedSource)
	}
	expectedTarget := id2
	if l.Target != expectedTarget {
		t.Errorf("link Target = %q, want %q", l.Target, expectedTarget)
	}
	expectedProperties := props
	if reflect.DeepEqual(l.Properties, expectedProperties) != true {
		t.Errorf("link Properties = %q, want %q", l.Properties, expectedProperties)
	}
}

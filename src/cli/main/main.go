package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {
	fmt.Println("    SucI: Slither surreptitiously!")
	scanner := bufio.NewScanner(os.Stdin)
	userInputParser := userInputParserGenerator()

	for {
		fmt.Print("---\n  SucurIndex > ")
		scanner.Scan()
		userInput := scanner.Text()
		commands, been_commanded := getCommands(userInput)
		if been_commanded == false {
			continue
		}

		command, available := userInputParser[commands.main]
		if !available {
			fmt.Println("    SucI: Unavailable command")
			continue
		}
		command.execution(commands.arguments)
	}
}

type Commands struct {
	main      string
	arguments []string
}

type Command struct {
	names       []string
	description string
	execution   func([]string)
}

var availableCommands = []Command{
	{
		names:       []string{"exit", "quit", "q"},
		description: "Exits SucurIndex",
		execution:   cliExit,
	},
	{
		names:       []string{"slither", "index-folder"},
		description: "Slithers through a folder and index its files",
		execution:   cliSLither,
	},
}

func getCommands(userInput string) (commands Commands, command_entered bool) {
	fields := strings.Fields(userInput)
	if len(fields) == 0 {
		return commands, false
	}
	commands.main = fields[0]
	commands.arguments = fields[1:]
	return commands, true
}

func userInputParserGenerator() (parser map[string]Command) {
	parser = map[string]Command{}
	for _, command := range availableCommands {
		for _, name := range command.names {
			parser[name] = command
		}
	}
	return parser
}

func cliExit(args []string) {
	if len(args) != 0 {
		fmt.Println("    SucI: Exit command takes no arguments")
		return
	}
	os.Exit(0)
}

func cliSLither(args []string) {
	if len(args) == 0 {
		fmt.Println(
			"    Suci: Must provide a the path of a directory that is to be " +
				"slithered through",
		)
		return
	}
	if len(args) > 1 {
		fmt.Println("    SucI: Slither command takes a single argument: " +
			"the path to a directory")
		return
	}
	fmt.Printf("    SucI: Slithering through %v\n", args[0])
}

// Package main is the entry-point for the go-sockets client sub-project.
// The go-sockets project is available under the GPL-3.0 License in LICENSE.
package main

import (
	"bufio"
	"encoding/base64"
	"encoding/json"
	"fmt"
	"net"
	"os"
	"strconv"
	"sync"
	"time"
)

// Application constants, defining host, port, and protocol.
const (
	connHost = "localhost"
	connPort = "3333"
	connType = "tcp"
)

var messageToServer = []string{}
var messageFromServer = [][]byte{}
var requestedData = []string{}

var wg sync.WaitGroup

func main() {
	wg.Add(1)
	// Start the client and connect to the server.
	fmt.Println("Connecting to", connType, "server", connHost+":"+connPort)
	conn, err := net.Dial(connType, connHost+":"+connPort)
	if err != nil {
		fmt.Println("Error connecting:", err.Error())
		os.Exit(1)
	}

	go waitForMessageToServer(conn)

	go waitForMessageFromServer(conn)

	// go handleConnection()

	go mainController()

	go handleReturns()

	wg.Wait()

}

func handleReturns() {
	for {
		// command, _ := reader.ReadString('\n')
		// messageToServer = append(messageToServer, command)
		if len(messageFromServer) > 0 {
			message := readMessageFromServer()
			messageType := fmt.Sprintf("%v", message["messageType"])
			// fmt.Println("Message:")
			// fmt.Println(message)
			switch messageType {
			case "returnRequestedData":
				// fmt.Println("Recived new output from player " + fmt.Sprintf("%v", message["playerId"]) + " in game " + fmt.Sprintf("%v", message["gamecode"]) + ":")
				decodedOutput, _ := base64.StdEncoding.DecodeString(fmt.Sprintf("%v", message["data"]))
				requestedData = append(requestedData, string(decodedOutput))
			}
		}
	}
}

func mainController() {
	response := false
	for !response {
		messageToServer = append(messageToServer, b64enc("{\"commandType\":\"do\",\"command\":\"Schritt\"}")+"\n")
		messageToServer = append(messageToServer, b64enc("{\"commandType\":\"get\",\"command\":\"IstWand\"}")+"\n")
		response, _ = strconv.ParseBool(waitForResponse())
	}
}

func waitForResponse() string {
	for len(requestedData) < 1 {
		time.Sleep(10 * time.Millisecond)
	}
	response := requestedData[0]
	requestedData = requestedData[1:]
	return response
}

func waitForMessageToServer(conn net.Conn) {
	for {
		if len(messageToServer) > 0 {
			//fmt.Println(messageToServer[0])
			conn.Write([]byte(messageToServer[0]))
			messageToServer = deleteFromArray(messageToServer, 0)
			time.Sleep(300 * time.Millisecond)
		}
	}
}

func waitForMessageFromServer(conn net.Conn) {
	for {
		buffer, err := bufio.NewReader(conn).ReadBytes('\n')
		if err != nil {
			fmt.Println("Server closed the connection.")
			wg.Done()
			// conn.Close()
			return
		}
		var message_raw = buffer[:len(buffer)-1]
		messageFromServer = append(messageFromServer, message_raw)
	}
}

func deleteFromArray(arr []string, pos int) []string {
	arr[pos] = arr[len(arr)-1]
	return arr[:len(arr)-1]
}

func readMessageFromServer() map[string]interface{} {
	// fmt.Println(strings.Replace(convertIntArrToStr(messageFromServer[0]), " ", "", -1))
	var messageRaw = b64dec(string(messageFromServer[0][2:]))
	//fmt.Println(messageRaw)
	var message map[string]interface{}
	if json.Unmarshal([]byte(messageRaw), &message) != nil {
		fmt.Println("Error decoding Message!")
		messageFromServer[0] = messageFromServer[len(messageFromServer)-1]
		messageFromServer = messageFromServer[:len(messageFromServer)-1]
		return nil
	}
	messageFromServer = messageFromServer[1:]
	return message
}

func convertIntArrToStr(arr []byte) string {
	return fmt.Sprintf("%c", arr)
}

func b64enc(input string) string {
	return base64.StdEncoding.EncodeToString([]byte(input))
}

func b64dec(input string) string {
	var result, _ = base64.StdEncoding.DecodeString(input)
	return string(result)
}

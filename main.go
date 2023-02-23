package main

import (
	"bytes"
	_ "embed"
	"fmt"
	"log"
	"os"
	"os/exec"
	"strings"

	"fyne.io/fyne"
	"fyne.io/fyne/app"
	"fyne.io/fyne/theme"
	"fyne.io/fyne/widget"
)

var runpy string
var cmd string = "\\bin\\app.py"
var runcmd *exec.Cmd

func main() {

	helptext := widget.NewLabel("")
	helptext2 := widget.NewLabel("")
	helptext3 := widget.NewLabel("")
	helptext4 := widget.NewLabel("")
	helptext5 := widget.NewLabel("")
	helptext6 := widget.NewLabel("")
	helptext7 := widget.NewLabel("")
	creatortext := widget.NewLabel("")
	creatortext2 := widget.NewLabel("github.com/ChrisCh4padia")
	Versionreference := widget.NewLabel("Release 1.0.0")

	Cameraoutput := widget.NewCheck("Original Cameraoutput", func(b bool) {})
	finalpic := widget.NewCheck("Keyed out picture", func(b1 bool) {})
	Backgroundpicture := widget.NewCheck("Orignal Backgroundpicture", func(b2 bool) {})
	Thresholdslider := widget.NewCheck("No Threshold Slider", func(b3 bool) {})
	Threshold := widget.NewCheck("Threshold", func(b5 bool) {})
	label := widget.NewLabel("Define Threshold (only applies if 'Treshold' is checked):")
	Thdecimal := widget.NewEntry()
	spacer := widget.NewLabel("")

	Launcher := widget.NewButtonWithIcon("Launch", theme.ConfirmIcon(), func() {

		helptext.Text = runpy + " cmd: " + cmd

		mydir, err := os.Getwd()
		if err != nil {
			fmt.Println(err)
		}
		mydir = mydir + cmd
		cmdexec := (strings.Replace(mydir, "\\", "/", -1))

		//check if the checkboxes are ticked and add the right parameters to the runcmd command

		args := []string{}
		if Cameraoutput.Checked {
			args = append(args, "-oi")
		}
		if finalpic.Checked {
			args = append(args, "-ok")
		}
		if Backgroundpicture.Checked {
			args = append(args, "-b")
		}
		if Thresholdslider.Checked {
			args = append(args, "-ns")
		}
		if Threshold.Checked {
			input := "-t " + Thdecimal.Text
			args = append(args, input)
		}
		vars := len(args)

		switch vars {
		case 0:
			runcmd = exec.Command("python3", cmdexec)
		case 1:
			runcmd = exec.Command("python3", cmdexec, args[0])
		case 2:
			runcmd = exec.Command("python3", cmdexec, args[0], args[1])
		case 3:
			runcmd = exec.Command("python3", cmdexec, args[0], args[1], args[2])
		case 4:
			runcmd = exec.Command("python3", cmdexec, args[0], args[1], args[2], args[3])
		case 5:
			runcmd = exec.Command("python3", cmdexec, args[0], args[1], args[2], args[3], args[4])
		default:
			runcmd = exec.Command("python3", cmdexec)
		}
		var out bytes.Buffer
		var stderr bytes.Buffer
		runcmd.Stdout = &out
		runcmd.Stderr = &stderr
		fmt.Println(runcmd)
		if err := runcmd.Run(); err != nil {
			fmt.Println(fmt.Sprint(err) + ": " + stderr.String())
			log.Fatal(err)
		}

	})

	contenttab1 := widget.NewVBox(Cameraoutput, finalpic, Backgroundpicture, Thresholdslider, Threshold, label, Thdecimal, spacer, Launcher, helptext)
	contenttab3 := widget.NewVBox(helptext, helptext2, helptext3, helptext4, helptext5, helptext6, helptext7)
	contenttab4 := widget.NewVBox(creatortext, creatortext2, Versionreference)

	app := app.New()
	w := app.NewWindow("Greenscreen-Chromakey")
	var tabs *widget.TabContainer
	var tab1, tab3, tab4 *widget.TabItem
	tab1 = widget.NewTabItemWithIcon("Home", theme.HomeIcon(), contenttab1)
	tab3 = widget.NewTabItemWithIcon("Help", theme.HelpIcon(), contenttab3)
	tab4 = widget.NewTabItemWithIcon("Contact", theme.WarningIcon(), contenttab4)
	tabs = widget.NewTabContainer(tab1, tab3, tab4)
	tabs.SetTabLocation(widget.TabLocationLeading)
	w.SetContent(tabs)
	w.Resize(fyne.Size{600, 350})
	w.ShowAndRun()
}

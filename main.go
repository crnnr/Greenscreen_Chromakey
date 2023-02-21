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
var vars string

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
	Thresholdslider := widget.NewCheck("Threshold Slider", func(b3 bool) {})
	fpsreader := widget.NewCheck("Fps reader", func(b4 bool) {})

	Launcher := widget.NewButtonWithIcon("Launch", theme.ConfirmIcon(), func() {

		if Cameraoutput.Checked {
			runpy = runpy + "1"
		}

		if finalpic.Checked {
			runpy = runpy + "2"
		}

		if Backgroundpicture.Checked {
			runpy = runpy + "3"
		}

		if Thresholdslider.Checked {
			runpy = runpy + "4"
		}

		if fpsreader.Checked {
			runpy = runpy + "5"
		}

		if strings.Contains(runpy, "1") {
			vars = vars + "-oi"
		}
		if strings.Contains(runpy, "2") {
			vars = vars + "-ok"
		}
		if strings.Contains(runpy, "3") {
			vars = vars + "-b"
		}
		if strings.Contains(runpy, "4") {
			vars = vars + "-ns"
		}
		if strings.Contains(runpy, "5") {
			vars = vars + "-nfps"
		}

		helptext.Text = runpy + " cmd: " + cmd

		mydir, err := os.Getwd()
		if err != nil {
			fmt.Println(err)
		}
		mydir = mydir + cmd
		cmdexec := (strings.Replace(mydir, "\\", "/", -1))
		runcmd := exec.Command("python3", cmdexec, vars)
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

	contenttab1 := widget.NewVBox(Cameraoutput, finalpic, Backgroundpicture, Thresholdslider, fpsreader, Launcher, helptext)
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

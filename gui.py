import PySimpleGUI as sg
import functions

sg.theme("default1")

label1 = sg.Text("Select Archive")
input1 = sg.Input()
button1 = sg.FileBrowse("Choose", key="archive")

label2 = sg.Text("Select Destination")
input2 = sg.Input()
button2 = sg.FolderBrowse("Choose", key="folder")

button_extract = sg.Button("Extract")
output_label = sg.Text(key="output", text_color="green")

button_exit = sg.Button("Exit")

window = sg.Window("Archive Extractor", layout=[[label1, input1, button1],
                                                [label2, input2, button2],
                                                [button_extract, output_label],
                                                [button_exit]])

while True:
    event, values = window.read()
    #print("1.event: ", event)
    #print("2.values: ", values)

    filepaths = values["archive"]
    folder = values["folder"]

    #print("3.filepaths: ", filepaths)
    #print("4.folder: ", folder)

    functions.extract_archive(filepaths, folder)
    window["output"].update(value="Extraction completed!")

    match event:
        case sg.WIN_CLOSED:
            break
        case "Exit":
            break

window.close()
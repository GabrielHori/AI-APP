const { app, BrowserWindow, ipcMain } = require("electron")
const path = require("path")

let win

app.whenReady().then(() => {
  win = new BrowserWindow({
    width: 1200,
    height: 800,
    frame: false, // IMPORTANT
    webPreferences: {
      preload: path.join(__dirname, "preload.js"),
    },
  })

  win.loadURL("http://localhost:5173") // ou fichier build
})

ipcMain.on("window:minimize", () => win.minimize())
ipcMain.on("window:maximize", () =>
  win.isMaximized() ? win.unmaximize() : win.maximize()
)
ipcMain.on("window:close", () => win.close())

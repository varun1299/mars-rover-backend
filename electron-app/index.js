const { app, BrowserWindow } = require('electron');
const path = require('path');
const { execFile } = require('child_process');

function createWindow () {
  const win = new BrowserWindow({
    width: 800,
    height: 600,
    webPreferences: {
      nodeIntegration: true
    }
  });

  win.loadURL('http://localhost:5000');  // URL where Flask app is running
}

app.whenReady().then(() => {
  // Start the Flask app
  const flaskApp = execFile('python', [path.join(__dirname, '../Backend/App.py')]);

  createWindow();

  app.on('activate', function () {
    if (BrowserWindow.getAllWindows().length === 0) createWindow();
  });

  flaskApp.stdout.on('data', function (data) {
    console.log(data.toString());
  });

  flaskApp.stderr.on('data', function (data) {
    console.error(data.toString());
  });

  flaskApp.on('close', function (code) {
    console.log('Flask app exited with code ' + code);
    app.quit();
  });
});

app.on('window-all-closed', function () {
  if (process.platform !== 'darwin') app.quit();
});

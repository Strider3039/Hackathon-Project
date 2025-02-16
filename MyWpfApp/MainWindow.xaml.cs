using System;
using System.Diagnostics;
using System.Threading.Tasks;
using System.Windows;

namespace WpfApp1
{
    public partial class MainWindow : Window
    {
        public MainWindow()
        {
            InitializeComponent(); // Ensure UI components are initialized
        }

        // Button click event to send "Make Sticker" message
        private async void Button_Click_3(object sender, RoutedEventArgs e)
        {
            this.Visibility = Visibility.Hidden;
            await RunPythonScriptAsync(@"..\main.py");
            this.Visibility = Visibility.Visible;
        }

        // Asynchronous method to run a Python script
        private async Task RunPythonScriptAsync(string scriptPath)
        {
            try
            {
                await Task.Run(() =>
                {
                    ProcessStartInfo psi = new ProcessStartInfo
                    {
                        FileName = "python",  // If Python isn't in PATH, provide full path to python.exe
                        Arguments = scriptPath,  // Python script file path
                        RedirectStandardOutput = true,
                        RedirectStandardError = true,
                        UseShellExecute = false,
                        CreateNoWindow = true
                    };

                    using (Process process = new Process { StartInfo = psi })
                    {
                        process.Start();
                        string output = process.StandardOutput.ReadToEnd();
                        string error = process.StandardError.ReadToEnd();
                        process.WaitForExit();

                        // Optionally, process the output or error
                        if (!string.IsNullOrWhiteSpace(error))
                        {
                            // Use Dispatcher to update the UI thread
                            Dispatcher.Invoke(() => MessageBox.Show("Error: " + error));
                        }
                        // If needed, you can also show the output:
                        // Dispatcher.Invoke(() => MessageBox.Show("Output: " + output));
                    }
                });
            }
            catch (Exception ex)
            {
                Dispatcher.Invoke(() => MessageBox.Show("Error: " + ex.Message));
            }
        }

        // Button click event to display gallery
        private async void Button_Click_2(object sender, RoutedEventArgs e)
        {
            await RunPythonScriptAsync(@"..\screenSticker.py");
        }

        // End program button
        private void Button_Click_1(object sender, RoutedEventArgs e)
        {
            this.Close();
        }

        // Open new window button
        private void OpenNewWindow_Click(object sender, RoutedEventArgs e)
        {
            NewWindow newWindow = new NewWindow();
            newWindow.Show();  // Open the new window
            // Optionally hide the current window: this.Hide();
        }
    }
}

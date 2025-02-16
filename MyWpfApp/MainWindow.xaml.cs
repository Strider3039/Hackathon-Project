using System.Text;
using System.Windows;
using System.Windows.Controls;
using System.Net.Sockets;
using System.Diagnostics;
using System;
using System.Threading.Tasks;  // For Task class


namespace WpfApp1
{
    public partial class MainWindow : Window
    {
        public MainWindow()
        {
           // InitializeComponent();
        }

        // Button click event to send "Make Sticker" message
        private void Button_Click_3(object sender, RoutedEventArgs e)
        {
            
            this.Visibility = Visibility.Hidden;
            RunPythonScript_Click(sender, e);
            this.Visibility = Visibility.Visible;
        }

        private async void RunPythonScript_Click(object sender, RoutedEventArgs e)
        {
            try
            {
                ProcessStartInfo psi = new ProcessStartInfo
                {
                    FileName = "python",  // If Python isn't in PATH, provide full path to python.exe
                    Arguments = @"..\main.py",  // Change this to your Python script's filename
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
                }
            }
            catch (Exception ex)
            {
                MessageBox.Show("Error: " + ex.Message);
            }
        }

        private void Button_Click_2(object sender, RoutedEventArgs e)
        {
            // display gallery
           // OpenNewWindow_Click(sender, e);
        }

        // end program button
        private void Button_Click_1(object sender, RoutedEventArgs e)
        {
           this.Close();
        }

        private void OpenNewWindow_Click(object sender, RoutedEventArgs e)
        {
            NewWindow newWindow = new NewWindow();
            newWindow.Show();  // Open the new window
            //this.Hide();  // Hide the current window (instead of closing it)
        }
    }
}


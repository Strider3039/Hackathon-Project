using System.Text;
using System.Windows;
using System.Windows.Controls;
using System.Net.Sockets;
using System.Diagnostics;

namespace WpfApp1
{
    public partial class MainWindow : Window
    {
        public MainWindow()
        {
            //InitializeComponent();
        }

        // Button click event to send "Make Sticker" message
        private void Button_Click_3(object sender, RoutedEventArgs e)
        {
            this.Visibility = Visibility.Hidden;
            RunPythonScript_Click(sender, e);
            this.Visibility = Visibility.Visible;
        }


        private void RunPythonScript_Click(object sender, RoutedEventArgs e)
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

                    MessageBox.Show("Output: " + output + "\nError: " + error);
                }
            }
            catch (Exception ex)
            {
                MessageBox.Show("Error: " + ex.Message);
            }
        }
        
        private void Button_Click_2(object sender, RoutedEventArgs e)
        {

        }

        // end program button
        private void Button_Click_1(object sender, RoutedEventArgs e)
        {
           // sendMessage("Kill");
        }
    }
}


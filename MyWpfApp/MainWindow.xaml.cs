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
            InitializeComponent();
        }

        private TcpClient client;  // Class-level field to hold the TcpClient
        private NetworkStream stream;  // Class-level field to hold the NetworkStream

        private void CloseConnectionToPython()
        {
            this.stream.Close();
            this.client.Close();
        }

        // Method to send message to the server
        public void sendMessage(string message)
        {
            if (client != null && client.Connected && stream != null && stream.CanWrite)
            {
                byte[] messageBytes = Encoding.ASCII.GetBytes(message);
                stream.Write(messageBytes, 0, messageBytes.Length);  // Send message to server
            }
            else
            {
                MessageBox.Show("Connection is closed or stream is not available.");
                // Optionally, try to reconnect here
               // ConnectToPythonBackend();
            }
        }

        // Button click event to send "Make Sticker" message
        private void Button_Click_3(object sender, RoutedEventArgs e)
        {
            this.WindowState = System.Windows.WindowState.Minimized;
            RunPythonScript_Click(sender, e);
            this.WindowState = System.Windows.WindowState.Normal;
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
        
    

    // Clean up resources when the window is closed
    private void Window_Closed(object sender, EventArgs e)
        {
            if (stream != null)
            {
                stream.Close();
            }
            if (client != null)
            {
                client.Close();
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


using System.Windows;
using System.Windows.Controls;  // For Image and other controls like Button, TextBox, etc.
using System.Windows.Media.Imaging;  // For BitmapImage
using System;
using System.Threading.Tasks;

namespace WpfApp1
{
    public partial class NewWindow : Window
    {
        public NewWindow()
        {
            InitializeComponent();
            this.Closed += NewWindow_Closed;

            AddImagesToGrid();
        }

        private void NewWindow_Closed(object sender, EventArgs e)
        {
            // When this window closes, open the main window
      //
        }

        public void run()
        {
            this.AddImagesToGrid(); // Add images to the grid
        }

        private void AddImagesToGrid()
        {
            // Example: Create 6 images and add them to the grid
            for (int row = 0; row < 3; row++) // Loop through rows
            {
                for (int col = 0; col < 2; col++) // Loop through columns
                {
                    Image img = new Image
                    {
                        Width = 100,
                        Height = 100,
                        Margin = new Thickness(5),
                        Source = new BitmapImage(new Uri($"Gallery/image{row * 2 + col + 1}.png", UriKind.Relative))
                    };

                    // Add the image to the grid
                    ImageGrid.Children.Add(img);

                    // Set the image's position in the grid
                    Grid.SetRow(img, row);
                    Grid.SetColumn(img, col);
                }
            }
        }

    }
}

using CmlLib.Core;
using CmlLib.Core.Auth;
using CmlLib.Core.Downloader;
using Newtonsoft.Json;
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace startmc
{
    public partial class Console : Form
    {
        public static StreamReader r = new StreamReader("LauncherInformation.json");
        public static string LI = r.ReadToEnd();
        LauncherInformation LauncherInformation = JsonConvert.DeserializeObject<LauncherInformation>(LI);
        public static bool HideState = false;
        public Console()
        {
            if (LauncherInformation.HideState == true)
            {
                HideState = true;
            }
            InitializeComponent();
            Run();
        }
        public async void Run()
        {
            try
            {   
                var path = LauncherInformation.Path;
                var launcher = new CMLauncher(path);
                var versions = await launcher.GetAllVersionsAsync();
                if (!File.Exists("VersionList.txt"))
                {
                    foreach (var item in versions)
                    {
                        File.AppendAllText("VersionList.txt", item.Name + "\n");
                    }
                }
                var launchOption = new MLaunchOption
                {
                    MaximumRamMb = LauncherInformation.Ram,
                    Session = MSession.GetOfflineSession(LauncherInformation.Name),
                    ScreenWidth = LauncherInformation.Width,
                    ScreenHeight = LauncherInformation.Height,
                };
                launcher.FileChanged += (e) =>
                {
                    listBox12.Items.Add("[{0}] {1} - {2}/{3}" + e.FileKind.ToString() + e.FileName + e.ProgressedFileCount + e.TotalFileCount);
                    listBox12.SelectedIndex = listBox12.Items.Count - 1;
                    listBox12.SelectedIndex = -1;
                };
                launcher.ProgressChanged += (s, e) =>
                {
                    progressBar1.Value = +e.ProgressPercentage;
                };
                
                var process = await launcher.CreateProcessAsync(LauncherInformation.Version, launchOption); // var process = await launcher.CreateProcessAsync("1.12.2-forge1.12.2-14.23.5.2838", launchOption); // forge                                                                                 // var process = await launcher.CreateProcessAsync("1.12.2-LiteLoader1.12.2"); // liteloader
                process.Start();
                this.Close();
                Application.Exit();
            }
            catch(Exception ex)
            {
                MessageBox.Show("Minecraft starter couldn't start, please make sure you have download it correctly.");
                this.Close();
                Application.Exit();
            }
        }

        private void Console_Load(object sender, EventArgs e)
        {
            if(HideState == true)
            {
                this.Hide();
                this.ShowInTaskbar = false;
            }
        }
    }
}

using System.Runtime.InteropServices;

namespace pythonTesting
{
    public class DataTransfer
    {
        public void transfer(string sourcePath, string destinationPath)
        {
            //if (Directory.Exists(sourcePath))
            //{
            //    int count = 0;
            //    foreach (var dict in new DirectoryInfo(sourcePath).GetDirectories())
            //    {
            //        string dictPath = sourcePath + "\\" + dict.Name;
            //        foreach (var file in new DirectoryInfo(dictPath).GetFiles())
            //        {
            //            if (file.Extension == ".txt")
            //            {
            //                string name = file.FullName;
            //                string filenum = count.ToString();
            //                File.Copy(file.FullName, destinationPath + "\\" + "file" + filenum + ".txt");
            //                count += 1;
            //            }
            //        }
            //    }
            //}
        }
    }
}

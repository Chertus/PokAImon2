# PowerShell script to arrange windows in a grid pattern
$processName = "python"  # The name of the process to arrange
$windows = @(Get-Process | Where-Object { $_.MainWindowTitle -like "*run_pretrained_interactive*" })

# Define the grid
$rows = 2
$cols = 5
$screenWidth = [System.Windows.SystemParameters]::PrimaryScreenWidth
$screenHeight = [System.Windows.SystemParameters]::PrimaryScreenHeight

# Calculate window size
$windowWidth = $screenWidth / $cols
$windowHeight = $screenHeight / $rows

# Arrange the windows
for ($i = 0; $i -lt $windows.Count; $i++) {
    $row = [Math]::Floor($i / $cols)
    $col = $i % $cols
    $x = $col * $windowWidth
    $y = $row * $windowHeight

    $hwnd = $windows[$i].MainWindowHandle
    $null = Add-Type -Namespace User32 -Name Functions -MemberDefinition '
        [DllImport("user32.dll")] public static extern bool MoveWindow(IntPtr hWnd, int X, int Y, int Width, int Height, bool Repaint);
    ' -PassThru

    $null::MoveWindow($hwnd, $x, $y, $windowWidth, $windowHeight, $true)
}

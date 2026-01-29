from PIL import Image, ImageDraw, ImageSequence
import colorsys
import sys
import subprocess
import importlib

try:
    sys.stdout.reconfigure(encoding='utf-8')
except AttributeError:
    pass


def auto_install(package_name):

    try:
        importlib.import_module("PIL")
    except ImportError:
        print(f"📦 偵測到尚未安裝 '{package_name}'，正在自動為您安裝...")
        try:
            subprocess.check_call(
                [sys.executable, "-m", "pip", "install", package_name])
            print(f"✅ {package_name} 安裝成功！繼續執行...")
        except Exception as e:
            print(f"❌ 自動安裝失敗: {e}")
            print(f"請手動在終端機輸入: pip install {package_name}")
            sys.exit(1)


auto_install("pillow")


def create_rainbow_bar_gif(filename, width=800, height=8, frames=60, duration=30):

    print(f"🚀 開始製作彩虹條: {width}x{height}px, 共 {frames} 幀...")

    images = []

    for frame_index in range(frames):
        img = Image.new('RGB', (width, height))
        draw = ImageDraw.Draw(img)

        hue_offset = frame_index / frames

        for x in range(width):

            x_ratio = x / width

            hue = (x_ratio * 1.0 + hue_offset) % 1.0

            saturation = 1.0
            value = 1.0

            r_float, g_float, b_float = colorsys.hsv_to_rgb(
                hue, saturation, value)
            rgb_color = (int(r_float * 255),
                         int(g_float * 255), int(b_float * 255))

            draw.line([(x, 0), (x, height)], fill=rgb_color)

        images.append(img)

        if (frame_index + 1) % 10 == 0 or frame_index == frames - 1:
            print(f"  - 已處理 {frame_index + 1}/{frames} 幀")

    print("💾 正在合成並儲存 GIF...")

    images[0].save(
        filename,
        save_all=True,
        append_images=images[1:],
        optimize=False,
        duration=duration,
        loop=0
    )
    print(f"✨ 大功告成！已輸出檔案: {filename}")


if __name__ == "__main__":

    output_filename = "github_rainbow_bar.gif"

    create_rainbow_bar_gif(
        filename=output_filename,
        width=880,
        height=8,
        frames=60,
        duration=25
    )

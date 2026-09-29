# 鹈鹕骑自行车测试 · 9 模型横评

题面：**一只骑自行车的鹈鹕**（零修饰词）。经典 AI 考题（致敬 Simon Willison），扔给内网 New API 中转站的 9 个模型：

- 文生图组 ×2：qwen-image-2.0-pro / wan2.7-image-pro
- SVG 组 ×5：qwen3.7-plus / qwen3.6-flash / deepseek-v4-pro / deepseek-v4-flash-0731 / glm-4.7-flash
- 特别参展：ZCode 手绘 SMIL 动态版（评测员亲自下场）
- 弃考：glm-5.3 / glm-5.3-flash（429，被评测员自己挤限流）

在线对比页：https://bayshier.github.io/pelican-bicycle/
完整文字版复盘：https://bayshier.github.io/GYZApp/blog-pelican-bicycle.html

`svg/` 目录是各模型的原始输出，未做任何修改。

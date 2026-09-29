# 鹈鹕骑自行车测试 · 9 个国产模型横评

一场**清一色国产阵容**的模型对比：智谱 GLM、阿里通义千问、DeepSeek、通义万相，全部走同一道经典考题——

> **一只骑自行车的鹈鹕**（零修饰词）

SVG 组先卷**代码与结构**（模型直接输出 SVG 代码，本文页面全部原样内嵌并注入 SMIL 动画，就在线上骑给你看），文生图组再卷**画面与题意**。

## 在线对比页

**https://bayshier.github.io/pelican-bicycle/**

## 参赛名单与结果

| 模型 | 组别 | 结果 | 一句话点评 |
|---|---|---|---|
| qwen3.7-plus | SVG | ✅ | 机械结构最严谨 |
| deepseek-v4-pro | SVG | ✅ | 细节狂魔，喉囊褶皱都画了 |
| deepseek-v4-flash-0731 | SVG | ✅ | 全场唯一挡泥板 + 腮红 |
| qwen3.6-flash | SVG | ✅ | 粗描边卡通，风格自洽 |
| glm-4.7-flash | SVG | ✅ | 踏板长在后轮轴上，没完全会 |
| qwen-image-2.0-pro | 文生图 | ✅ | 题意天花板：端坐踩踏 + 小皮鞋 |
| wan2.7-image-pro | 文生图 | ✅ | 美术第一，但鹈鹕在摆拍 |
| glm-5.3 / glm-5.3-flash | SVG | ❌ 429 | 被评测员自己挤限流 |

`svg/` 目录为各模型原始输出（未修改的静态原版），线上页面为其注入了 SMIL 动画（车轮旋转 · 整车颠簸 · 曲柄蹬踏 · 链条流动）。

## 完整复盘

文字版：https://bayshier.github.io/GYZApp/blog-pelican-bicycle.html

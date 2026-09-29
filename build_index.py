#!/usr/bin/env python3
"""从 svg/ 与 img/ 重建 index.html（含 SMIL 动画注入说明）"""
import re
from pathlib import Path

R = Path(__file__).parent

def svg_inline(path, note):
    svg = Path(path).read_text()
    root = re.match(r'(<svg[^>]*>)', svg).group(1)
    root_clean = re.sub(r'\s(width|height)="[^"]*"', '', root, count=1)
    svg = root_clean + svg[len(root):]
    return f'<figure class="fig"><div class="box">{svg}</div><figcaption>{note}</figcaption></figure>'

cards = {
 'qwen37': svg_inline(R/'svg/qwen3.7-plus.svg', 'qwen3.7-plus · 机械最严谨 · 动画：轮转+链条流动+曲柄蹬踏'),
 'dsv4pro': svg_inline(R/'svg/deepseek-v4-pro.svg', 'deepseek-v4-pro · 细节狂魔 · 动画：轮转(additive)+链条+曲柄'),
 'dsv4flash': svg_inline(R/'svg/deepseek-v4-flash-0731.svg', 'deepseek-v4-flash-0731 · 唯一挡泥板 · 动画：轮转+曲柄'),
 'qwen36': svg_inline(R/'svg/qwen3.6-flash.svg', 'qwen3.6-flash · 粗描边卡通 · 动画：轮转+曲柄'),
 'glm47': svg_inline(R/'svg/glm-4.7-flash.svg', 'glm-4.7-flash · 动画：轮转+颠簸（踏板长在后轮轴，曲柄不转）'),
 'zcode': svg_inline(R/'svg/鹈鹕骑自行车-动态.svg', 'ZCode 手绘动态版 · 评测员下场（本页即是活的动画）'),
}

T = Path(R/'template.html').read_text() if (R/'template.html').exists() else None
# 模板不存在时从头生成（与首版一致，仅更新 SVG 组说明与 captions）
T = '''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>鹈鹕骑自行车 · 9 模型横评</title>
<style>
  :root{--bg:#0e1116;--card:#171c24;--line:#262d38;--fg:#e6ebf2;--dim:#8b95a5;--green:#34d399;--blue:#60a5fa;--amber:#fbbf24;--red:#f87171;}
  *{box-sizing:border-box;margin:0;padding:0}
  body{background:var(--bg);color:var(--fg);font:15px/1.8 -apple-system,"PingFang SC","Microsoft YaHei",sans-serif;padding:34px 28px;max-width:1240px;margin:0 auto}
  h1{font-size:26px;margin-bottom:6px}
  h2{font-size:19px;margin:34px 0 14px;padding-left:12px;border-left:4px solid var(--green)}
  .sub{color:var(--dim);font-size:13px;margin-bottom:8px}
  .grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(430px,1fr));gap:18px}
  .card{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:16px}
  .card h3{font-size:15px;margin-bottom:10px}
  .tag{font-size:11px;padding:2px 9px;border-radius:20px;margin-left:8px;vertical-align:2px}
  .t-img{background:#12332a;color:var(--green)} .t-svg{background:#1a2333;color:var(--blue)}
  .t-spec{background:#3a2c12;color:var(--amber)} .t-fail{background:#3b1d1d;color:var(--red)}
  .box{background:#fff;border-radius:10px;padding:8px}
  .box svg{width:100%;height:auto;display:block;max-height:560px}
  img{width:100%;height:auto;display:block;border-radius:10px}
  .fig{margin-bottom:6px}
  figcaption{color:var(--dim);font-size:12.5px;margin-top:8px;text-align:center}
  table{width:100%;border-collapse:collapse;font-size:14px;margin-top:6px}
  th,td{border:1px solid var(--line);padding:8px 12px;text-align:left}
  th{background:#1a212c;color:var(--dim);font-weight:500}
  footer{margin-top:40px;color:var(--dim);font-size:12.5px;border-top:1px solid var(--line);padding-top:16px}
  a{color:var(--blue)}
</style>
</head>
<body>
<h1>🚲 鹈鹕骑自行车测试 · 9 模型横评</h1>
<div class="sub">题面：一只骑自行车的鹈鹕（零修饰词） · 赛场：内网 New API 中转站 192.168.1.61:3000 · 2026.09 · 7 交卷 / 2 限流弃考</div>

<h2>一、文生图组</h2>
<div class="grid">
  <div class="card"><h3>qwen-image-2.0-pro<span class="tag t-img">题意天花板</span></h3>
    <img src="img/qwen-image-2.0-pro.jpg" alt="qwen-image-2.0-pro">
    <p class="sub">端坐车座、脚踩踏板——还给鹈鹕穿了黑色小皮鞋。</p></div>
  <div class="card"><h3>wan2.7-image-pro<span class="tag t-img">最美但没骑</span></h3>
    <img src="img/wan2.7-image-pro.jpg" alt="wan2.7-image-pro">
    <p class="sub">黄金时刻光影全场第一，但鹈鹕在车架上摆拍，没在骑。</p></div>
</div>

<h2>二、SVG 组 · 全员动态骑行<span class="tag t-svg">SMIL 动画注入：车轮旋转 · 整车颠簸 · 曲柄蹬踏 · 链条流动</span></h2>
<div class="grid">
  <div class="card"><h3>qwen3.7-plus<span class="tag t-svg">机械最严谨</span></h3>{qwen37}</div>
  <div class="card"><h3>deepseek-v4-pro<span class="tag t-svg">细节狂魔</span></h3>{dsv4pro}</div>
  <div class="card"><h3>deepseek-v4-flash-0731<span class="tag t-svg">唯一挡泥板</span></h3>{dsv4flash}</div>
  <div class="card"><h3>qwen3.6-flash<span class="tag t-svg">粗描边卡通</span></h3>{qwen36}</div>
  <div class="card"><h3>glm-4.7-flash<span class="tag t-svg">踏板在后轮轴</span></h3>{glm47}</div>
</div>
<p class="sub">SVG 组为模型原作 + 注入 SMIL 动画（保持原坐标不动，只加动画元素）；未加动画的原始版本在 git 历史与博客存档中。</p>

<h2>三、特别参展：ZCode 手绘动态版<span class="tag t-spec">评测员下场 · 本页即动画</span></h2>
<div class="card">{zcode}
<p class="sub">纯坐标手绘 + SMIL 原生动画（零 JS）：车轮旋转 · 双腿 180° 相位蹬踏 · 链条双向流动 · 整车颠簸 · 头部点动 · 云朵飘移 · 速度线掠过。</p></div>

<h2>四、弃考席</h2>
<div class="card"><h3>glm-5.3 / glm-5.3-flash<span class="tag t-fail">429 弃考</span></h3>
<p class="sub">全程 429 Too Many Requests，换三把 key 无效（通道级拥堵）。最讽刺的原因：评测脚本与评测员（ZCode 会话）共用同一条 glm 通道——裁判下场参赛，把自己挤出局。</p></div>

<h2>五、评分表</h2>
<table>
  <tr><th>模型</th><th>机械结构</th><th>鹈鹕特征</th><th>「骑」的动作</th><th>一句话点评</th></tr>
  <tr><td>qwen-image-2.0-pro</td><td>★★★★★</td><td>★★★★★（+小皮鞋）</td><td>✅ 端坐踩踏</td><td>题意理解天花板</td></tr>
  <tr><td>wan2.7-image-pro</td><td>★★★★☆</td><td>★★★★★</td><td>❌ 站着摆拍</td><td>美术第一，题意跑偏</td></tr>
  <tr><td>qwen3.7-plus</td><td>★★★★★</td><td>★★★★☆</td><td>⚠️ 脚没踩实</td><td>SVG 机械结构最严谨</td></tr>
  <tr><td>deepseek-v4-pro</td><td>★★★★☆</td><td>★★★★★（喉囊褶皱）</td><td>✅ 双腿双踏板</td><td>细节狂魔</td></tr>
  <tr><td>deepseek-v4-flash-0731</td><td>★★★★☆</td><td>★★★★☆（+挡泥板+腮红）</td><td>✅ 双腿双踏板</td><td>小而全，会卖萌</td></tr>
  <tr><td>qwen3.6-flash</td><td>★★★☆☆</td><td>★★★★☆</td><td>✅ 腿在踏板上</td><td>粗描边卡通，风格自洽</td></tr>
  <tr><td>glm-4.7-flash</td><td>★☆☆☆☆</td><td>★★☆☆☆</td><td>❌ 腿悬空</td><td>交了卷，但没完全会</td></tr>
  <tr><td>ZCode 手绘动态版</td><td>★★★★★</td><td>★★★★☆</td><td>✅ 动态蹬踏中</td><td>评测员亲自下场</td></tr>
  <tr><td>glm-5.3 / glm-5.3-flash</td><td colspan="4">— 429 弃考 —</td></tr>
</table>

<footer>题面致敬 Simon Willison 的经典 LLM 视觉测试 · 完整文字版复盘见 <a href="https://bayshier.github.io/GYZApp/blog-pelican-bicycle.html">博客文章</a> · 原始 SVG 文件在 <a href="https://github.com/bayshier/pelican-bicycle/tree/main/svg">svg/ 目录</a> · 2026.09</footer>
</body>
</html>
'''

html = (T.replace('{qwen37}', cards['qwen37']).replace('{dsv4pro}', cards['dsv4pro'])
        .replace('{dsv4flash}', cards['dsv4flash']).replace('{qwen36}', cards['qwen36'])
        .replace('{glm47}', cards['glm47']).replace('{zcode}', cards['zcode']))
(R / 'index.html').write_text(html)
print('index.html 重建:', len(html) // 1024, 'KB（SVG 组已全部动态化）')

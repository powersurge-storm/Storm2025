# ASE WAND USER GUIDE
**Quick Reference for Field Operation** | Team PowerSurge Storm

---

## ⚡ QUICK START

1. Open browser → Go to: **https://powersurge-storm.github.io/Storm2025/wand_page.html**
2. Tap **⚙️** → Enter Pi IP address → Select models
3. Ready to use!

---

## 🎮 6-TAB NAVIGATION

```
┌──────────────────────────────────────────────────────────────────┐
│  🎤 Record  |  🗺️ Site GPR  |  📡 Depth LiDAR  |  🏺 Artifact AI  |  📋 Summary  |  ⚙️  │
└──────────────────────────────────────────────────────────────────┘
```

---

## 📝 1. 🎤 RECORD - Voice Documentation

**[SCREENSHOT: Record screen with START RECORDING button]**

```
┌─────────────────────────┐
│   Voice Recording       │
│                         │
│   Status: Ready         │
│                         │
│   🔴 START RECORDING   │
│                         │
└─────────────────────────┘
```

**How to Use:**
1. Tap **🎤 Record** tab
2. Tap **🔴 START RECORDING**
3. Speak observations clearly (15-20 cm from mic)
4. Tap **⏹️ STOP RECORDING**
5. Auto-transcribed, timestamped, GPS-tagged

**Tips:** Use short phrases • Say "comma" or "period" • 99 languages supported

---

## 🗺️ 2. SITE GPR - Subsurface Detection

**[SCREENSHOT: Site GPR screen with CAPTURE & DETECT button]**

```
┌─────────────────────────┐
│   Site GPR              │
│                         │
│   📷 CAPTURE & DETECT  │
│                         │
│   📸 USE PI CAMERA     │
│                         │
└─────────────────────────┘
```

**How to Use:**
1. Tap **🗺️ Site GPR** tab
2. Position device over ground
3. Tap **📷 CAPTURE & DETECT** (or **📸 USE PI CAMERA**)
4. AI detects subsurface anomalies
5. Results show depth and confidence

**Detects:** Buried artifacts • Soil disturbances • Underground structures

---

## 📡 3. DEPTH LiDAR - 3D Surface Mapping

**[SCREENSHOT: Depth LiDAR screen with buttons]**

```
┌─────────────────────────┐
│   Depth LiDAR           │
│                         │
│   Loading AI...         │
│                         │
│   📷 CAPTURE & DETECT  │
│                         │
│   📸 USE PI CAMERA     │
└─────────────────────────┘
```

**How to Use:**
1. Tap **📡 Depth LiDAR** tab
2. Hold 30-50 cm above surface
3. Tap **📷 CAPTURE & DETECT**
4. Creates 3D depth map with measurements
5. Scan in grid pattern for complete coverage

**Maps:** Topography • Excavation depth • Artifact dimensions • Layers

---

## 🏺 4. ARTIFACT AI - Identification

**[SCREENSHOT: Artifact AI screen with RUN SCAN button]**

```
┌─────────────────────────┐
│   Artifact AI           │
│                         │
│   Ready to scan         │
│                         │
│   📏 RUN SCAN          │
│                         │
└─────────────────────────┘
```

**How to Use:**
1. Tap **🏺 Artifact AI** tab
2. Point camera at artifact
3. Tap **📏 RUN SCAN**
4. AI identifies type + confidence %
5. Review recommendation

**17 Types:** Pottery • Stone Tools • Metal • Bone • Shell • Textile • Wood • Glass • Brick • Debitage • Beads • Projectile Points • Grinding Stones • Fire-Cracked Rock • Charcoal • Seeds • Other

**Confidence:** 90-100% (high/green) • 70-89% (medium/yellow) • <70% (low/flag for review)

---

## 📋 5. SUMMARY - Session Review

**[SCREENSHOT: Summary screen showing session data]**

**How to Use:**
1. Tap **📋 Summary** tab
2. Review all session data:
   - Voice recordings & transcripts
   - GPR scans & detections  
   - LiDAR depth maps
   - AI classifications
3. Verify completeness
4. Export/sync to lab

---

## ⚙️ 6. SETTINGS - Configuration

**[SCREENSHOT: Settings screen with configuration options]**

```
┌────────────────────────────┐
│  Configuration         ×   │
│                            │
│  🔗 GET NGROK URL         │
│  Current ngrok URL:        │
│  [url displayed]           │
│  📋 COPY URL              │
│                            │
│  Pi IP/URL: [input]        │
│  Artifact Model: [select]  │
│  Site Model: [select]      │
└────────────────────────────┘
```

**Setup:**
1. Tap **⚙️** (gear icon)
2. Enter **Pi IP/URL**
3. Select **Artifact Model** + **Site Model**
4. Tap **🔗 GET NGROK URL** for remote lab access
5. Tap **📋 COPY URL** to share with team

---

## 🔄 TYPICAL WORKFLOW

**MORNING:**
```
⚙️ Settings → Enter Pi IP → 🎤 Record → "Site: [name], Date: [date]"
```

**SURVEY:**
```
🗺️ Site GPR → CAPTURE → Mark detections → 📡 Depth LiDAR → CAPTURE → Map surface
```

**EXCAVATE:**
```
🏺 Artifact AI → RUN SCAN → Review confidence → 🎤 Record → Describe findings
```

**EVENING:**
```
📋 Summary → Review data → Export to lab
```

---

## 🔧 QUICK TROUBLESHOOTING

| Problem | Fix |
|---------|-----|
| **Recording won't start** | Check mic permissions • Refresh page |
| **"Loading AI..." stuck** | Verify Pi IP in ⚙️ Settings • Check WiFi |
| **Camera not working** | Enable camera permissions • Clean lens |
| **Low AI confidence** | Better lighting • Multiple angles • Cleaner image |
| **Cannot connect to Pi** | Check Pi IP is correct • Pi on same network • Restart Pi |
| **Ngrok URL not working** | Check internet • Restart ngrok on Pi |

---

## ✅ FIELD CHECKLIST

**BEFORE LEAVING:**
□ Charge Raspberry Pi & tablet  
□ Test URL: https://powersurge-storm.github.io/Storm2025/wand_page.html  
□ ⚙️ Settings → Enter Pi IP  
□ Test 🎤 Record + 📷 Camera  

**AT SITE:**
□ Connect to WiFi/hotspot  
□ Verify Pi connection (⚙️)  
□ Generate ngrok URL for lab  
□ Start with 🎤 Record (site info)  

**WORKFLOW:**
□ 🗺️ GPR scan grid  
□ 📡 LiDAR map surface  
□ 🏺 AI identify artifacts  
□ 🎤 Record all observations  
□ 📋 Summary before leaving  

---

## 📱 DEVICE REQUIREMENTS

**Browsers:** Chrome, Firefox, Safari, Edge  
**Devices:** Tablet (recommended) • Phone • Laptop  
**Permissions:** Camera ✓ • Microphone ✓ • JavaScript ✓  
**Connection:** WiFi or cellular internet

---

## 🎯 BEST PRACTICES

**Recording:**
- Start: "Site: [name], Date: [date], Archaeologist: [name]"
- Short phrases (10-15 sec)
- Consistent terminology

**Scanning:**
- Grid pattern with 20% overlap
- Hold steady at correct distance
- Multiple passes confirm findings

**AI Usage:**
- Trust 90%+ confidence
- Verify 70-89% with expert
- Flag <70% for review
- Multiple angles improve accuracy

---

## 📊 QUICK REFERENCE TABLE

| Tab | Button | Distance | Purpose | Time |
|-----|--------|----------|---------|------|
| 🎤 | START RECORDING | 15-20 cm | Voice notes | 10-30 sec |
| 🗺️ | CAPTURE & DETECT | Over ground | Subsurface | 5-10 sec |
| 📡 | CAPTURE & DETECT | 30-50 cm | 3D depth map | 5-10 sec |
| 🏺 | RUN SCAN | Point at artifact | AI classify | 1-2 sec |
| 📋 | (review) | - | Session data | As needed |
| ⚙️ | (config) | - | Setup/remote | 2-5 min |

---

**ASE Wand User Guide v2.0** | Team PowerSurge Storm | FLL 2025-2026  
**Interface:** https://powersurge-storm.github.io/Storm2025/wand_page.html  
**Support:** support@asewand.com

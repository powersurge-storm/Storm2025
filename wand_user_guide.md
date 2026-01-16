# ASE WAND USER GUIDE
**Quick Reference for Field Operation** | Team PowerSurge Storm

---

## ⚡ QUICK START

1. Open browser → Go to: **https://powersurge-storm.github.io/Storm2025/wand_page.html**
2. Tap **⚙️** → Enter Pi IP address → Select models
3. Ready to use!

---

## 🎮 6-TAB NAVIGATION

<img width="62" height="380" alt="image" src="https://github.com/user-attachments/assets/58195388-be9e-4212-a0ba-325d9a2ea43f" />

## 📝 1. 🎤 RECORD - Voice Documentation

<img width="616" height="298" alt="image" src="https://github.com/user-attachments/assets/a85d5b2a-24f9-4d0c-af39-5175230e1d1e" />


**How to Use:**
1. Tap **🎤 Record** tab
2. Tap **🔴 START RECORDING**
3. Speak observations clearly (15-20 cm from mic)
4. Auto-transcribed, timestamped, GPS-tagged

**Tips:** Use short phrases • Say "comma" or "period" • 99 languages supported

---

## 🗺️ 2. SITE GPR - Subsurface Detection

<img width="605" height="288" alt="image" src="https://github.com/user-attachments/assets/607c88db-f643-4a21-90a8-8a30eb86acc5" />

**How to Use:**
1. Tap **🗺️ Site GPR** tab
2. Position device over ground
3. Tap **📷 CAPTURE & DETECT** (or **📸 USE PI CAMERA**)
4. AI detects subsurface anomalies
5. Results show depth and confidence

**Detects:** Buried artifacts • Soil disturbances • Underground structures

---

## 📡 3. DEPTH LiDAR - 3D Surface Mapping

<img width="598" height="292" alt="image" src="https://github.com/user-attachments/assets/9d83ffba-ad75-4b62-9491-e424ee5befcb" />


**How to Use:**
1. Tap **📡 Depth LiDAR** tab
2. Hold 30-50 cm above surface
3. Tap **📷 DEPTH MAP**
4. Creates 3D depth map with measurements
5. Scan in grid pattern for complete coverage

**Maps:** Topography • Excavation depth • Artifact dimensions • Layers

---

## 🏺 4. ARTIFACT AI - Identification

<img width="601" height="285" alt="image" src="https://github.com/user-attachments/assets/d81085e0-431b-4bf4-b11b-321f88d9c259" />

**How to Use:**
1. Tap **🏺 Artifact AI** tab
2. Point camera at artifact
3. Tap **📏 DETECT ARTIFACT**
4. AI identifies type + confidence %
5. Review recommendation

**17 Types:** Pottery • Stone Tools • Metal • Bone • Shell • Textile • Wood • Glass • Brick • Debitage • Beads • Projectile Points • Grinding Stones • Fire-Cracked Rock • Charcoal • Seeds • Other

**Confidence:** 90-100% (high/green) • 70-89% (medium/yellow) • <70% (low/flag for review)

---

## 📋 5. SUMMARY - Session Review

<img width="606" height="309" alt="image" src="https://github.com/user-attachments/assets/a3b4a887-ade8-452d-97f0-0e29948559fb" />

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

<img width="559" height="293" alt="image" src="https://github.com/user-attachments/assets/7472d7b0-22ef-4993-9b4e-aa41c5453129" />

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

## 📊 QUICK REFERENCE TABLE

| Tab | Button | Distance | Purpose | Time |
|-----|--------|----------|---------|------|
| 🎤 | START RECORDING | 15-20 cm | Voice notes | 10-30 sec |
| 🗺️ | DETECT SITE | Over ground | Subsurface | 5-10 sec |
| 📡 | DEPTH MAP | 30-50 cm | 3D depth map | 5-10 sec |
| 🏺 | DETECT ARTIFACT | Point at artifact | AI classify | 1-2 sec |
| 📋 | (review) | - | Session data | As needed |
| ⚙️ | (config) | - | Setup/remote | 2-5 min |

---

**ASE Wand User Guide v2.0** | Team PowerSurge Storm | FLL 2025-2026  
**Interface:** https://powersurge-storm.github.io/Storm2025/wand_page.html  
**Support:** support@asewand.com

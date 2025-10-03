# NASA-app-challenge

# Title Slide
**Through the Radar Looking Glass: Revealing Earth Processes with SAR**
_Subtitle_: Case Study – Sikkim Flood, June 2025  
👨‍💻 Arnab Satpati | B.Tech CSE (AI/ML)  

---

# Slide 1: Introduction
**Title:** Why Study Floods with SAR?  
- Floods = recurrent Himalayan hazard  
- Cloud cover during monsoon → optical sensors fail  
- SAR (Synthetic Aperture Radar) penetrates clouds & works day/night  
- Our Aim: Build ML model to detect potential floods using SAR data  

**Script:**  
"Floods in the Himalayas are devastating and hard to monitor in real time because optical satellites fail under heavy cloud cover. SAR gives us an all-weather, all-time view, making it a powerful tool for early flood warning. Our project uses SAR data to teach machines how to detect floods before they escalate."

---

# Slide 2: The Sikkim Flood, June 1, 2025
**Title:** Disaster Snapshot  
- Excessive rainfall triggered flash floods  
- Major impact zones: Chungthang, Mangan, Lachen-Lachung valleys  
- Key infrastructure damaged: Teesta-III Dam (Chungthang), Dikchu HEP, bridges, NH-10  
- Hundreds displaced, power projects crippled  

**Script:**  
"On June 1, 2025, Sikkim witnessed severe flooding caused by excessive rainfall. Chungthang and Mangan were among the worst-hit areas, with hydropower dams like Teesta-III severely damaged. Roads, bridges, and villages were swept away, making this one of the most destructive incidents in recent years."

---

# Slide 3: Linking Rainfall to Floods
**Title:** Rainfall as the Primary Driver  
- IMD data: >200 mm rain in 24 hours in North Sikkim  
- Steep terrain + saturated slopes = flash floods & landslides  
- River Teesta swelled beyond safe capacity  
- Dams became bottlenecks, worsened downstream flooding  

**Script:**  
"Excessive rainfall was the main trigger. In less than 24 hours, North Sikkim received more than 200 millimeters of rain. With already saturated slopes, the river Teesta overflowed. Hydropower dams couldn’t contain the surge, creating a domino effect downstream."

---

# Slide 4: SAR’s Role in Flood Monitoring
**Title:** What SAR Reveals  
- Backscatter difference = water detection  
- Interferometric coherence = landslide identification  
- Pre- and post-flood SAR pairs highlight changes  
- Sentinel-1 IW mode → 10 m resolution, free access  

**Script:**  
"SAR reveals what’s invisible to the naked eye. By comparing backscatter and coherence between pre- and post-event images, we can detect inundated zones and landslides. Sentinel-1, with free access, is our main data source."

---

# Slide 5: Study Area & AOIs
**Title:** Key Affected Zones  
- **Upstream:** South Lhonak glacial lake, Chungthang, Teesta-III  
- **Midstream:** Dikchu hydro project, Lachen & Lachung valleys  
- **Downstream:** NH-10 washed bridges, Gangtok outskirts, Mangan district  
- Control areas: unaffected river bends  

**Script:**  
"Our AOIs cover the upstream source at South Lhonak and Chungthang, midstream at Dikchu and the valleys, and downstream sections where roads and bridges collapsed. We’ll also use nearby unaffected sites as controls."

---

# Slide 6: Data Collection Strategy
**Title:** Data Sources  
- **SAR:** Sentinel-1 GRD & SLC (pre- and post-event)  
- **Optical:** Sentinel-2, PlanetScope for ground truth  
- **DEM:** SRTM, ALOS World 3D for topography  
- **Reports:** NDMA, IMD rainfall data for validation  

**Script:**  
"Our dataset integrates Sentinel-1 SAR with optical imagery for validation, DEMs for topographic correction, and official reports for labeling. The SAR-first approach ensures reliability even under heavy clouds."

---

# Slide 7: Preprocessing Pipeline
**Title:** Preparing SAR for ML  
- Orbit correction & radiometric calibration  
- Speckle filtering & terrain correction  
- Backscatter conversion (σ0 in dB)  
- Generate coherence maps  
- Tile into 256×256 patches for ML  

**Script:**  
"Before training, SAR data needs careful preprocessing — calibration, speckle filtering, terrain correction, and tiling. We’ll use both backscatter intensity and coherence layers as ML inputs."

---

# Slide 8: ML Model Approach
**Title:** Flood Detection Model  
- Input: VV, VH, coherence, difference layers  
- Model: U-Net segmentation for flood masks  
- Binary classification: flooded / not flooded  
- Future: multi-class (flood, landslide, infrastructure damage)  

**Script:**  
"We start with a U-Net model trained on SAR inputs like VV, VH, coherence, and difference images. The model will generate flood masks for binary classification. Later, we aim for multi-class classification to detect landslides and infrastructure damage."

---

# Slide 9: Why This Matters
**Title:** Impact & Applications  
- Early flood warning → saves lives  
- Infrastructure risk monitoring (dams, bridges)  
- Policy-level decision support  
- Expands Earth observation science with SAR  

**Script:**  
"Our work goes beyond academic value. With SAR-based ML, we can provide early flood warnings, monitor critical infrastructure like dams, and support policy decisions. It’s a step toward resilient disaster management."

---

# Slide 10: Conclusion & Next Steps
**Title:** Wrapping Up  
- Excessive rainfall = key driver of Sikkim floods  
- SAR = reliable eye through clouds & night  
- ML models can automate flood detection  
- Next step: Build dataset, train baseline model, expand to multi-class  

**Script:**  
"In conclusion, the Sikkim flood shows how excessive rainfall can turn catastrophic in fragile mountain ecosystems. SAR allows us to see through clouds and night, making it ideal for flood monitoring. With ML, we can automate detection and provide timely insights. Our next steps are dataset creation, baseline model training, and scaling to multi-class flood-risk mapping."

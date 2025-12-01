languages = {
    "en": "English",
    "hi": "Hindi",
    "kn": "Kannada"
}

translations = {
    "en": {
        "home": "Home",
        "dashboard": "Dashboard",
        "predict": "Predict",
        "contact": "Contact",
        "community": "Community",
        "about": "About",
        "login": "Login",
        "profile": "Profile",
        "resetpassword": "Reset Password",
        "language": "Language",
    },

    "hi": {
        "home": "मुख्य पृष्ठ",
        "dashboard": "डैशबोर्ड",
        "predict": "पूर्वानुमान",
        "contact": "संपर्क",
        "community": "समुदाय",
        "about": "बारे में",
        "login": "लॉगिन",
        "profile": "प्रोफ़ाइल",
        "resetpassword": "पासवर्ड रीसेट",
        "language": "भाषा",
    },

    "kn": {
        "home": "ಮುಖಪುಟ",
        "dashboard": "ಡ್ಯಾಶ್‌ಬೋರ್ಡ್",
        "predict": "ಭವಿಷ್ಯವಾಣಿ",
        "contact": "ಸಂಪರ್ಕ",
        "community": "ಸಮುದಾಯ",
        "about": "ಬಗ್ಗೆ",
        "login": "ಲಾಗಿನ್",
        "profile": "ಪ್ರೊಫೈಲ್",
        "resetpassword": "ಪಾಸ್ವರ್ಡ್ ಮರುಹೊಂದಿಸಿ",
        "language": "ಭಾಷೆ",
    }
}

def translate(key, lang="en"):
    if lang not in translations:
        lang = "en"  # fallback
    return translations[lang].get(key, key)

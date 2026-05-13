import instaloader

# Create an instance
L = instaloader.Instaloader()

# Target profile
target = "akt8085"

# Download the profile (profile_pic_only=True skips posts/stories)
L.download_profile(target, profile_pic_only=True)
print(f"Profile data for {target} downloaded!")

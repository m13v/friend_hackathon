from mem0 import Memory
import os
from dotenv import load_dotenv
import json

load_dotenv()

# Temporarily set the API key directly (for testing purposes only)

# Initialize the Memory class
memory = Memory()

# Add a new memory
# raw_data = """
# 0 notifications total

# Skip to search

# Skip to main content

# Keyboard shortcuts
# Close jump menu
# Search
# new feed updates notifications
# Home
# 3
# 3 new network updates notifications
# My Network
# Jobs
# 2
# 2 new messages notifications
# Messaging
# 9
# 9 new notifications
# Notifications
# Matthew Diakonov
# Me

# For Business
# Get 50% Off Sales Nav
# Background Image
# Nik Shevchenko
# Nik has a premium account
# Click to upgrade to Premium
# test
# Nik Shevchenko
#   1st degree connection1st
# Thiel Fellow | 2x Founder | Looking for hardware cofounder nikshevchenko.com

# Based Hardware
# San Francisco Bay Area  Contact info
# Looking for hardware cofounder 
# 15,113 followers 
# 500+ connections


# Rocky Yu, Julia Chimisova 🇺🇦, and 156 other mutual connectionsRocky Yu, Julia Chimisova 🇺🇦, and 156 other mutual connections

# Message

# More
# HighlightsHighlights
# Company logo
# Nik was recently hiredNik was recently hired
# Nik started their role at Based Hardware 4 months ago.Nik started their role at Based Hardware 4 months ago.
# Free insight from Sales NavigatorFree insight from Sales Navigator
# Unlock more Sales Navigator insights
# See who has viewed your profile, recently changed jobs, followed your company and more.

# Get Sales Navigator
# Cancel anytime, for any reason.

# AboutAbout
# Short: 24yo, Thiel Fellow, sold 2 startups (last one I scaled to $52m valuation, raised $3m and sold it to toptal.com)
# ------
# Long: Hey, I'm Nik Shevchenko, founder of fundplatform.io (sold) and WeLoveNoCode.com, launched in 2020 to accelerate product development through no-code solutions and sold to toptal.com in 2023. 

# With a background in developing over 15 no-code applications, I drive quick product deployment to meet business objectives.

# My leadership was shown in hiring more than 100+ team members and in securing more than $3 million seed funding

# Based in San Francisco, I prioritize team-building and talent acquisition. I am actively engaged in staffing, recruiting, and leading dedicated teams towards achieving innovative solutions in the tech industry.

# My core skills include:
# - No-code platforms (Bubble, Adalo, Zapier, Webflow, Tilda, Airtable, Notion etc.)
# - Project Management
# - Product Management
# - Staffing and Recruiting
# - Fundraising and Financial Management
# - Team Building and Leadership
# - Problem-Solving and Troubleshooting
# - Robotics, VR/AR

# What do I like: Recruiting, VR/AR, robotics and longevity but open to anything else where I can bring value

# My motto: Be smart enough to look for smart people, because you are not the smartest.Short: 24yo, Thiel Fellow, sold 2 startups (last one I scaled to $52m valuation, raised $3m and sold it to toptal.com) ------ Long: Hey, I'm Nik Shevchenko, founder of fundplatform.io (sold) and WeLoveNoCode.com, launched in 2020 to accelerate product development through no-code solutions and sold to toptal.com in 2023. With a background in developing over 15 no-code applications, I drive quick product deployment to meet business objectives. My leadership was shown in hiring more than 100+ team members and in securing more than $3 million seed funding Based in San Francisco, I prioritize team-building and talent acquisition. I am actively engaged in staffing, recruiting, and leading dedicated teams towards achieving innovative solutions in the tech industry. My core skills include: - No-code platforms (Bubble, Adalo, Zapier, Webflow, Tilda, Airtable, Notion etc.) - Project Management - Product Management - Staffing and Recruiting - Fundraising and Financial Management - Team Building and Leadership - Problem-Solving and Troubleshooting - Robotics, VR/AR What do I like: Recruiting, VR/AR, robotics and longevity but open to anything else where I can bring value My motto: Be smart enough to look for smart people, because you are not the smartest.
# Top skillsTop skills
# Business Strategy • Hiring • Business Management • Strategy • FundraisingBusiness Strategy • Hiring • Business Management • Strategy • Fundraising
# FeaturedFeatured
# PostPost
# Today I randomly posted an AI wearable project on Kickstarter 

# In a few hours it overachieved the goal by 250% and blew up on twitter

# I'm excited to announce that from today, I'm working on FRIEND

# It's an open source AI wearable that records, summarizes and gives feedback on your conversations

# It costs only $39 and allows anyone to build the apps they want

# Here is how it works:

# likelovecelebrate
# 180
# 23 comments
# PostPost
# 📢 I'm very excited to announce that Toptal has acquired WLNC

# Our journey at WLNC has been eventful and tumultuous – as many startups endeavors are. Today, however, we're excited to share that Toptal, the top platform for on-demand talent, has acquired us. This move paves the way for expansive growth in the no-code sector, backed by Toptal's vast resources.

# Why Toptal? Their scale and success will enable our growth, making them an ideal partner for realizing our vision. Our customers will transition smoothly to Toptal's platform, ensuring continuous access to trusted services. Our experts will soon have the chance to join Toptal's network.

# A huge thank you to our customers, experts, investors, and advisors for their continuous support. Kudos to our dedicated team, including Alex Hudym, Daniel Gorenko, Manal Rayess, Daniel Baise, Caio Kaspary, and everyone else who helped along the journey, for making this possible.

# Some team members will join Toptal, while others pursue new paths. If you're hiring, consider our talented team ready for new roles: https://rb.gy/oa20o

# What's next: I am excited to start a new company right away! I will be exploring new avenues such as VR/AR, Robots, Longevity, and more. If you are working on something cool or have an interest in any of these industries, reach out to me at kodjima33@gmail.com. You can also discover my thoughts on the future here: https://lnkd.in/eXgprh7B

# hashtag#WeLoveNoCode hashtag#Toptal hashtag#Acquisition hashtag#NoCode hashtag#VR hashtag#Metaverse

# likecelebratelove
# 696
# 190 comments
# PostPost
# A few years ago, I embarked on a journey from the middle of nowhere to San Francisco with a dream and a vision. Today, I'm proud to be at the helm of WLNC, a no-code talent marketplace that bridges gaps and creates opportunities for people who can't relocate

# Here are three lessons I've learned along the way:
# Embrace Diversity: Moving from Russia to San Francisco taught me the value of diverse perspectives. Our platform thrives because we celebrate differences and believe in the power of global collaboration.

# Resilience is Key: Building a startup is never a straight path. There have been challenges, but each setback has been a setup for a bigger comeback. To every young entrepreneur out there, remember that persistence pays off.

# Community Matters: San Francisco's vibrant tech community has been instrumental in our growth. The support, mentorship, and connections I've found here are unparalleled.

# To everyone who's been a part of this journey, thank you. And to those just starting out, remember: every big dream begins with a single step. Keep moving forward!

# hashtag#entrepreneurship hashtag#startupjourney hashtag#SanFrancisco hashtag#talentmarketplace"
# No alternative text description for this image
# likecelebratelove
# 176
# 14 comments
# LinkLink

# 3 Things I Believe Will Change the World3 Things I Believe Will Change the World
# nikshevchenko.substack.comnikshevchenko.substack.com
# TL:DR: Metaverse / Robots / LongevityTL:DR: Metaverse / Robots / Longevity
# PostPost
# How to successfully raise funding and grow a startup to $130K MRR in less than a year? Happy to share my learning 👇

# My name is Nik and I'm the founder of WLNC, a platform that connects businesses with the best no code developers to build software and applications without a single line of code. 

# Having just raised $1M in seed funding, broke through the $130k MRR barrier, formed the biggest no-code marketplace (3k+ no-code developers) — I have learned a lot.

# Find all of the best tips from my practical experience which can help you grow.



# P.S.: If you want to join a fast-growing rocketship, message me. 


# hashtag#startup hashtag#nocodelowcode 
# hashtag#fundingnews

# $130k MRR and $1M raised: 8 Lessons Learned
# Nik Shevchenko on LinkedIn • 5 min read
# likecelebratelove
# 64
# 10 comments

# ActivityActivity
# 15,113 followers15,113 followers


# Following

# Posts

# Comments

# Videos

# Images
# Loaded 3 Posts posts
# Nik Shevchenko posted this • 1d1d
# We are top-1 on Product Hunt Thank you everyone for your support! https://lnkd.in/eM8C8PRF

# We are top-1 on Product Hunt

# Thank you everyone for your support! https://lnkd.in/eM8C8PRF
# likecelebratelove
# 69
# 5 comments
# Nik Shevchenko posted this • 1d1d
# Meet your Friend on Product Hunt today To celebrate the launch, giving 5 devices to 5 random supporters! - Upvote - Leave a comment Results on Monday https://lnkd.in/eM8C8PRF

# Meet your Friend on Product Hunt today

# To celebrate the launch, giving 5 devices to 5 random supporters! 

# - Upvote
# - Leave a comment

# Results on Monday

# https://lnkd.in/eM8C8PRF…show more
# likecelebratelove
# 67
# 15 comments
# Nik Shevchenko posted this • 4d4d
# This weekend we gave 100+ FRIEND AI necklaces to the hackathon participants After seeing 12+ amazing demos, we selected 4 best teams, who will get $2k+ in credits and 10+ devices! Congrats! This hackathon skyrocketed our user numbers => we've crossed 2k FRIEND users! See you all next Saturday at the AI wearables hackathon!
# No alternative text description for this image
# This weekend we gave 100+ FRIEND AI necklaces to the hackathon participants

# After seeing 12+ amazing demos, we selected 4 best teams, who will get $2k+ in credits and 10+ devices! Congrats!

# This hackathon skyrocketed our user numbers => we've crossed 2k FRIEND users! 

# See you all next Saturday at the AI wearables hackathon!…show more
# likecelebratelove
# 57
# 7 comments
# 1 repost
# Show all posts
# ExperienceExperience
# Based Hardware logo
# FounderFounder
# Based Hardware · Full-timeBased Hardware · Full-time
# Apr 2024 - Present · 4 mosApr 2024 to Present · 4 mos
# San Francisco, California, United StatesSan Francisco, California, United States
# 1) What1) What
# The Thiel Foundation logo
# Thiel FellowThiel Fellow
# The Thiel FoundationThe Thiel Foundation
# Feb 2023 - Present · 1 yr 6 mosFeb 2023 to Present · 1 yr 6 mos
# WLNC logo
# FounderFounder
# WeLoveNoCode · Full-timeWeLoveNoCode · Full-time
# Dec 2020 - Oct 2023 · 2 yrs 11 mosDec 2020 to Oct 2023 · 2 yrs 11 mos
# San Francisco Bay AreaSan Francisco Bay Area
# Acquired by toptal.comAcquired by toptal.com
# On Deck logo
# On Deck Scale FellowshipOn Deck Scale Fellowship
# On DeckOn Deck
# Sep 2022 - Dec 2022 · 4 mosSep 2022 to Dec 2022 · 4 mos
# San Francisco Bay AreaSan Francisco Bay Area
# Fund Platform logo
# FounderFounder
# Fund PlatformFund Platform
# May 2017 - Apr 2020 · 3 yrsMay 2017 to Apr 2020 · 3 yrs
# AcquiredAcquired
# Show all 6 experiences
# Licenses & certificationsLicenses & certifications
# WLNC logo
# Certified Bubble DeveloperCertified Bubble Developer
# WLNCWLNC
# Issued Jun 2022Issued Jun 2022
# Show credential
# Reforge logo
# Reforge (4 courses) 
# Reforge (4 courses) 
# ReforgeReforge
# Issued Jan 2022Issued Jan 2022
# Show all 6 licenses & certifications
# SkillsSkills
# Business ManagementBusiness Management

# Endorsed by 2 people in the last 6 monthsEndorsed by 2 people in the last 6 months
# 2 endorsements2 endorsements

# Endorse
# StrategyStrategy

# Endorsed by 2 people in the last 6 monthsEndorsed by 2 people in the last 6 months
# 2 endorsements2 endorsements

# Endorse
# Show all 10 skills
# RecommendationsRecommendations
# Recommend Nik
# ReceivedReceived
# GivenGiven
# Nothing to see for nowNothing to see for now
# Recommendations that Nik receives will appear here.Recommendations that Nik receives will appear here.
# InterestsInterests
# Top VoicesTop Voices
# CompaniesCompanies
# GroupsGroups
# SchoolsSchools

# """  # Truncated for brevity
# user_id = "nik124912412841962839"
# agent_id = "friend_01"
# run_id = "test_run"
# metadata = {"type": "profile"}
# memory_response = memory.add(data=raw_data, user_id=user_id, agent_id=agent_id, run_id=run_id, metadata=metadata)
# print(f"Memory response: {memory_response}")
# # Retrieve the memory by ID
# memory_id = memory_response[0]['id']
# retrieved_memory = memory.get(memory_id)
# print(f"retrieved_memory: {retrieved_memory}")

# Extract a profile summary
def extract_profile_summary(memory_item):
    if os.getenv('OPENAI_API_KEY'):
        user_id = memory_item['metadata']['user_id']
        all_user_memories = memory.get(user_id="nik124912412841962839")
        print(f"all_user_memories={all_user_memories}")
        related_memories = memory.search(query=f"Tell me everything about {user_id}", user_id=user_id)
        return related_memories
    else:
        print("OPENAI_API_KEY is not set. Skipping memory addition.")
        return None
    
def extract_by_userid(user_id):
    if os.getenv('OPENAI_API_KEY'):
        # all_memories = memory.get_all()
        # memory_id = all_memories[0]["id"] # get a memory_id
        # print(f"all_user_memories={all_memories}")
        # print(f"memory_id={memory_id}")
        related_memories = memory.search(query=f"Tell me everything about {user_id}", user_id=user_id)
        return related_memories
    else:
        print("OPENAI_API_KEY is not set. Skipping memory addition.")
        return None

# niksprofile=extract_by_userid("nik124912412841962839")
# print(niksprofile)

# profile_summary = extract_profile_summary(retrieved_memory)
# print(profile_summary)
# [{'id': '7bc8509d-5f44-4e51-8d56-eab9708b3b68', 'text': '### Facts\n- Name: Nik Shevchenko\n- Age: 24\n- Location: San Francisco Bay Area\n- Thiel Fellow\n- Founder of Based Hardware\n- Founder of WeLoveNoCode (WLNC), sold to Toptal in 2023\n- Founder of fundplatform.io, sold\n- Developed over 15 no-code applications\n- Raised $3 million in seed funding\n- Scaled a startup to a $52 million valuation\n- Hired more than 100 team members\n- Actively engaged in staffing, recruiting, and leading teams\n- Launched an AI wearable project called FRIEND\n- FRIEND is an open-source AI wearable that records, summarizes, and gives feedback on conversations\n- FRIEND costs $39\n- FRIEND has over 2,000 users\n- Participated in On Deck Scale Fellowship\n- Certified Bubble Developer\n- Completed 4 courses at Reforge\n- Has 15,113 followers on LinkedIn\n- Has 500+ connections on LinkedIn\n\n### Preferences\n- Likes recruiting, VR/AR, robotics, and longevity\n- Open to anything where he can bring value\n- Motto: "Be smart enough to look for smart people, because you are not the smartest."\n\n### Memories\n- Recently hired at Based Hardware\n- Started role at Based Hardware 4 months ago\n- WLNC was acquired by Toptal\n- Excited to start a new company focusing on VR/AR, robots, and longevity\n- Moved from Russia to San Francisco\n- Learned the value of diverse perspectives, resilience, and community support\n- FRIEND AI wearable project overachieved its Kickstarter goal by 250% and gained traction on Twitter\n- Gave 100+ FRIEND AI necklaces to hackathon participants, resulting in 12+ demos and 4 best teams receiving $2k+ in credits and 10+ devices', 'metadata': {'type': 'profile', 'user_id': 'nik', 'agent_id': 'friend_01', 'run_id': 'test_run', 'data': '### Facts\n- Name: Nik Shevchenko\n- Age: 24\n- Location: San Francisco Bay Area\n- Thiel Fellow\n- Founder of Based Hardware\n- Founder of WeLoveNoCode (WLNC), sold to Toptal in 2023\n- Founder of fundplatform.io, sold\n- Developed over 15 no-code applications\n- Raised $3 million in seed funding\n- Scaled a startup to a $52 million valuation\n- Hired more than 100 team members\n- Actively engaged in staffing, recruiting, and leading teams\n- Launched an AI wearable project called FRIEND\n- FRIEND is an open-source AI wearable that records, summarizes, and gives feedback on conversations\n- FRIEND costs $39\n- FRIEND has over 2,000 users\n- Participated in On Deck Scale Fellowship\n- Certified Bubble Developer\n- Completed 4 courses at Reforge\n- Has 15,113 followers on LinkedIn\n- Has 500+ connections on LinkedIn\n\n### Preferences\n- Likes recruiting, VR/AR, robotics, and longevity\n- Open to anything where he can bring value\n- Motto: "Be smart enough to look for smart people, because you are not the smartest."\n\n### Memories\n- Recently hired at Based Hardware\n- Started role at Based Hardware 4 months ago\n- WLNC was acquired by Toptal\n- Excited to start a new company focusing on VR/AR, robots, and longevity\n- Moved from Russia to San Francisco\n- Learned the value of diverse perspectives, resilience, and community support\n- FRIEND AI wearable project overachieved its Kickstarter goal by 250% and gained traction on Twitter\n- Gave 100+ FRIEND AI necklaces to hackathon participants, resulting in 12+ demos and 4 best teams receiving $2k+ in credits and 10+ devices', 'created_at': 1722131203}, 'score': 0.36150792498633627}]

def extract_by_memory_id(memory_id):
    if os.getenv('OPENAI_API_KEY'):
        print(f"Extracting profile for memory_id: {memory_id}")
        
        try:
            # Get the specific memory
            memories = memory.get_all(user_id="nik124912412841962839")
            print("Memories:")
            for m in memories:
                print(f"- {m['text']}")
                
            memory_item = memory.get(memory_id)
            print(f"Memory item: {json.dumps(memory_item, indent=2)}")

            if memory_item:
                user_id = memory_item.get('metadata', {}).get('user_id')
                if user_id:
                    print(f"Searching for memories related to user {user_id}")
                    related_memories = memory.search(query=f"Tell me everything about {user_id}", user_id=user_id)
                    print(f"Related memories: {json.dumps(related_memories, indent=2)}")
                    return related_memories
                else:
                    print(f"No user_id found in metadata for memory_id: {memory_id}")
                    return None
            else:
                print(f"No memory found for memory_id: {memory_id}")
                return None
        except Exception as e:
            print(f"Error retrieving memory: {str(e)}")
            return None
    else:
        print("OPENAI_API_KEY is not set. Skipping memory operations.")
        return None

# Example usage
memory_id = "945f76bd-3393-4182-b266-10020cd7a76a"
profile = extract_by_memory_id(memory_id)
print(f"Profile: {json.dumps(profile, indent=2)}")
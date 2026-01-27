## 2025-12-05 - MBARI Success Criteria Kickoff

**Meeting Recording:** https://app.attention.tech/conversations/all-calls/e2e56450-2c02-42ea-b68d-4e1506ed1af3

**Voxel 51 Participants:**

- Azriel Nicdao
- Sid Mehta
- Praveen Palem

**MBARI Participants:**

- Danelle Cline
- Laura Chrobak

**Meeting Notes:**

- Initial kickoff meeting with team introductions (Azriel, Sid, Praveen from Voxel51; Danelle and Laura from MBARI)
- Discussed SSO setup requirements and credential management (OAuth/Google Auth vs internal SSO)
- Covered FiftyOne Enterprise vs Open Source key differences (cloud file paths, multiplayer, managed database)
- Reviewed dataset structure: 10,000 human-reviewed phytoplankton labels (cropped ROIs) needing cleanup
- Discussed S3 bucket setup with read/write permissions for cloud storage
- Planned workflow: embeddings visualization → similarity search → model evaluation → zero-shot prediction
- Established Slack channel for async communication and weekly sync meetings
- Next steps: SSO configuration, S3 bucket setup, deployment provisioning

### Transcript

00:01 Azriel Nicdao
So, oh, I was supposed to leave at 11:00 AM I ended up leaving at like 9:00 PM or something like that.

00:07 Danelle Cline
So A long way over.

00:09 Azriel Nicdao
Oh my. Yeah. And it wasn't reassuring 'cause the pilot was like, yeah, you know, it was delayed because of a maintenance issue. I was like a maintenance issue. And he was just talking about how like the whatever was happening, he was just like, yeah, we can't seem to start the engine so we have to like keep rehiring the engine.

00:30 Danelle Cline
Oh My goodness.

00:31 Azriel Nicdao
He's like, but it's okay. We're still safe to fly. We're like, Hmm, okay My, But I'm here so I have made it. Hi Laura.

00:48 Danelle Cline
Hi Laura.

00:49 Laura Chrobak
Hi.

00:51 Azriel Nicdao
Perfect. Looks like we have quorum. Let's go ahead and get started. First of all, thank you guys for jumping on board. There are a couple of housekeeping things. I was talking to Dr. Henry and looks like we're trying to wrap things up. I sent him over that PDF, so I think he's having some folks review it and then he will send me back a signed copy and then after we'll have to sign in and send it back over to y'all. But hopefully we can get that done the latest probably Monday end of day. Do you guys know if that's a, a timeline that will work or do I have to spin up something new?

01:34 Laura Chrobak
I pinged Henry about this yesterday and he hasn't responded. Let me double check on that and I'll alert him to the deadline as well.

01:43 Azriel Nicdao
Okay, sounds good. Yeah, I wanted to intro Sid and Pravin who will be helping y'all out. Can you guys spun up? I had shared over some of those initial timelines and goals that you created in that document, so that was really helpful for us to just have a ground zero for where we're starting to get deployed, get your guys' data in, do the workflows and all that. So that was really helpful. Sid, you wanna introduce yourself Pravin and then we can kind of go from there.

02:14 Sid Mehta
Yeah, sounds good. Nice to meet you all. My name's Sid. I'm based out here in Scottsdale, Arizona, in the Phoenix area, so kind of remote first company here at 51. So people all over the country. Yeah, I've been here around eight months. Mainly work with customers who after, you know, if they've decided that they wanna purchase 51 Enterprise, I kind of work with them, make sure they can get up and running with 51 Enterprise. It integrates into their infrastructure and then work with them to also make sure that they can run the workflows and integrations that they want to do. So I've been here around eight months and before this I was at a ML X company called Comet. I'm not sure if you're familiar, but it's one DB MLO kind of equivalent. So I've been working with kinda machine learning teams for the past three years and before that I, I trained models, which seemed like ages ago at at Intel. So live the life of a computer vision developer in a past life at this point. So, but yeah, I'll pass it on to my colleague Pravin.

03:11 Praveen Palem
Hey y'all, my name's Pravin. I'm based here in Austin, Texas. Joined the company recently and I'll be tag teaming with Sid and you know, kind ensuring that your goals are met and you know, kind of responsible for the, for the, for this account essentially. But, but Sid is going to be the subject matter expert 'cause he's been here longer and he's awesome at what he does. And being my background is, you know, almost 10 years in AI ml. I've been in the customer facing role. I've also built models at General Motors, most recently computer visual models. But I've also been in similar roles at startups implementing solutions for customers. So I guess, you know, we've been around the block and I'm excited to be working and such use, cool use cases involving marine life and whatnot.

04:06 Azriel Nicdao
So thank you for having, Maybe you could introduce yourselves, Danielle, and, and Laura for, for them. I think that would be great. I know you guys quite well, so Can you guys hear me okay?

04:28 Danelle Cline
So yeah, I, I work with folks here and my day-to-day, I'm a senior software developer and I work on machine learning pipelines, audio video images across different science projects here. I've been doing machine learning for a long time, different, different aspects of it, but we're excited to be working with you guys on this particular project because it's challenging and we feel like the tool has some great capabilities that we really need here. And I'm speaking, I'm coming from a place of someone who's actually had to spin up my own tools and develop and modify tools and I, I really appreciate and understand how much work, how much work it is and I'm excited to be working with you and Laura on this. What's it? Hi everyone. Hi everyone. Sorry I just a really big Lunchtime also Having lunch.

05:42 Laura Chrobak
Here's Laura. I am a currently an ML ops research engineer with the FM net program, which is a program that one of the PIs here runs that creates a lot of models and a database and a game all around computer vision and working with ecologists. I'm also, I work with Danelle on the SUSE project, which is really focused on class fires for phytoplankton. And my background is in applied computer vision for the ocean space primarily. So I've been working in that niche for a long time and yeah, I'm super excited to get spun up on these tools. It will be definitely unlocking a lot of our work stream, so thanks.

06:31 Sid Mehta
Cool. Yeah. Cool. Awesome. Yeah, thanks so much for the intro. So I think just on our end what we'd like to do on these calls is that we like to learn a bit more about your use case. It also sounds like you guys might have used 51 open source in the past, right? So you're kind of familiar with some of the terminology. So we just, you know, wanna make sure that we understand as much as we can about your use case. Also, thanks so much for sending your kind of goals and timelines to az. That's great. That's honestly something that we don't normally get, so it's nice. So you know that you guys have that and you know, we, we tend to ma we wanna match your guys' energy as well. It seems like you guys are really wanting to get started soon. So we'll, we'll try to match that. And then also we'll just go over kind of, you know, just some housekeeping stuff about, you know, communication and all that type of stuff with time succinct and then also the info questions that I'll need so we can get you guys up and running and then I'll kind of, you know, just wrap it up in a bow and say what we want for next steps. So does that sound like a good agenda? Awesome. Cool. Yeah, so, okay. Am I hearing myself? Is that just me? Yeah. And you guys are based in the, what area are you guys in?

07:36 Danelle Cline
We are in Moss Landing, which is, I don't know, maybe an hour and a half south of San Francisco.

07:46 Sid Mehta
Ah, okay, got it, got it. Okay, so you're close enough to where AZ can walk from Sacramento is what I'm hearing. Maybe a, a decent walk for him so, but okay, cool. All right, so first question, I guess it sounds like you have used 51 open source, so I'm just curious like what are kind of like the data formats that you mainly work with? What maybe type of label types that you're hoping to visualize within the tool? I guess have both of you kind of played with the open source or is it just you Laura?

08:16 Danelle Cline
It's a little bit, I think Laura's probably a little deeper than Yeah, we, I'm, I think Danella as well.

08:27 Laura Chrobak
I'm very familiar with lots of different platforms of this genre. I've used internal Google tools in my last role I have used Robo Flow, I've used VLO 51 both like as an individual and in coursework when I was at Michigan. And then there are a bunch of similar types of tools specifically in the ocean world. So I have lots of familiarity there in terms terms of our data and this specific project, we're working mostly with classifiers. So it's all of our images are actually cropped ROIs and we don't really have, we're, we're not gonna be dealing with the whole image in this case. We're just gonna send you directly the ROI, we have about 10,000 human reviewed labels so far for this project, but they're not super clean. So we definitely wanna do some maintenance there. And we currently have one classifier that we've trained using these labels in terms of the data format, they're currently formatted actually, I mean they're currently in Tater, which is another platform similar to all of these. But we can get them to you in any format that you so believe.

09:55 Danelle Cline
I actually did an exercise where I, to get familiar with the tools, exported the data and then imported it. It took about half a day, it was so, so API's really nice. So we have a way to get the data out and the data into the tool. I think that's probably pretty straightforward. And you know, our data's labeled as Laura says, we, we already have the image, it's been pulled out, but we have class names, scores, secondary class names in some cases. So we might have some more flexible metadata that we wouldn't like anybody Right. Would wanna visualize. But the, a real challenge in the data sets are one, they can be really large if we're just working with the training data that's so far pretty small, but we would like to run it on a lot more data. So visualizing millions of points, millions of images within a collection is of interest. And another challenge is the images are ambiguous and domain specific. So some of the foundational models may not work really well because they're just not in the model. And planktons really diverse and challenging And we do have some experts that will be looking at it. So our users will be us of course to do the mechanical things, but the, there'll be some science users.

11:43 Sid Mehta
And so where is like your, these like cropped images and like even the full images, like do you guys use like a cloud? So like somewhere in the cloud where all this data is stored?

11:55 Danelle Cline
No, we don't at the moment, but we have cloud accounts, we have a relationship with Amazon and Subaccounts set up. Okay. We can, we can certainly put them easily in the cloud if that's needed. Got it. That's not a problem.

12:08 Sid Mehta
Got it. Okay, cool. Yeah that's good because most of the, so the big difference between 51 enterprise and 51 open source, right? Is open source is, you know, single player local data with enterprise it's on the, it's you know, multiplayer and then generally your data is like stored in the cloud. So people have their data in, you know, Google's cloud storage buckets, Azure buckets, a lot of people who stored in S3. So, and then it's pretty easy, right? And just instead of the file path, it's local file path. It's just a global S3 file path and all you have to do is just set the credentials there and into the platform. And we'll go through all over this but, okay, so it sounds good.

12:44 Danelle Cline
So you do have like an S3 bucket where we can put all these images that we, We can, we're gonna have to set up an account for this particular project. Okay. But that's pretty straightforward.

12:53 Sid Mehta
Okay, got it.

12:54 Danelle Cline
And then we can, we can upload them and make them, I, I presume public to simplify things, right?

13:02 Sid Mehta
Yeah.

13:03 Danelle Cline
By public you mean The security on the bucket?

13:07 Sid Mehta
Oh yeah, yeah, yeah, yeah. So basically you'll upload credentials and whatever credentials the, whatever buckets the credentials have access to, it'll only show those credentials. So there'll be global cred, there'll be global credentials. So like anyone who has access to feature and enterprise will inherit those credentials. But yeah, like if you know those credentials don't have access to a bucket A then bucket A images in bucket A won't be shown. Only images like B, C or D will be shown. So that's, so yeah we can do, we can get to that level if needed.

13:37 Danelle Cline
Okay, so single credential shared across all. Yeah. And they'll have the need to have full access. Yeah, yeah, yeah, yeah. Reading to reading full read access to the book.

13:50 Sid Mehta
Yeah. Although, yeah, reading, we generally recommend write in some cases as well. Sometimes there might be some instances where you might need to write to the bucket. So it might just, if it's, you know, no trouble, I generally recommend, especially I don't like, I don't know if you ever will do like video data, but sometimes with video data we, we convert it to frames and then we write frames for the buckets. But in general I would recommend if, if possible, if security allows to, to make it also a rideable bucket just In case.

14:16 Danelle Cline
Yeah, that's fine. It's, I, I don't see any problem with that.

14:19 Sid Mehta
Perfect. Cool. Okay, so sounds like I will be using S3 as kind of that kind of cloud storage backend. Okay, got it. And then, yeah, I mean what you were saying makes a lot of sense. You have some labels it sounds like the classification labels, right? I know they're on the ROI, so one thing also that we can talk about is that we have this ability to where you can, you can put the full images and then if you have the ROIs as well, like we have a thing called patches view and a lot of people use that. So you can put the full images on there, but if you have the crop ROIs as well, we can work that way. We're very flexible. But yeah, the classification labels, it's, it's good. It sounds like that you have ground truth labels that you wanna kind of like annotate and we can kind of show you what people do for embeddings workflows to kind of QA that and, and some of the clustering stuff that we have. But then it also sounds like you have model predictions as well, which is really exciting. 'cause then you can use the evaluation features. So would you say that more or less, so you know the curation part of it find quality assurance and then also the model evaluation. Are those kind of the main workflows you're looking to do? Or is there anything else in the platform that you guys were kind of hoping to get up and running soon?

15:21 Laura Chrobak
Yeah, I think that I put, I think some key Got it elements that we were interested in somewhere in here. Ha. Okay so these like Danelle and our team just put in really high level, yeah. The specific workflow that we're interested in tackling in this three month period. So this would be like first obviously getting images available in cloud and accessible with the tool. Then we wanna do a refinement exercise. So with the 10,000 labels that we already have, we want, we have some collaborators who are gonna reconcile. Some of those have different, we're labeled with one label map and then a second one if you wanna reconcile those. The step after that would be potentially running our existing model over a new batch of data and then generating new labels through this process. And we want to basically, I think just to give you a sense of, do I say put some example of scale? No. So each deployment that we have has almost a million ROI output. And so we're not planning on having a human review all of those. But in this step three, when we run that model over these, we wanna leverage the similarity search and the clustering to bulk review. And then also mine for our rare classes. 'cause those are our, our two big class, two big tasks. And then finally retrain with that new set and evaluate our performance on some withheld test set. And I think like a really big goal that I'm hoping for is I put some context about our cycle cadence this past year. So this will show you how long we spent doing the process, how many labels we had generated. It doesn't, for example, v the V three output, you'll see it's, there's only 720 from those. But they were very, they we focused on rare classes. So this took much longer despite the quality. Anyways, the point is we're really curious to see how these tools kind of accelerate the, the cycle that we've seen from the past.

17:45 Sid Mehta
Yeah, got It. Got it. Makes sense. Yeah, no, no, thanks so much. That's so helpful. And then one thing what we and Pravin can do is that we can kind of take this, I believe AZ shared with us as, but we can kind of take it and start populating like, okay these are your workflows that you have or these are your things and what in 51 can you do to kind of like help in that? So we'll, we'll we'll kind of help and work with the mappings for you. So I think it sounds good. Awesome. Yeah, so I think I have everything. I feel like I need to kind of understand your use cases, where you're coming from. I guess Pravin, were there any other questions you had on your end?

18:17 Praveen Palem
One question. Sorry, go ahead.

18:20 Danelle Cline
Well I, this is great. Seems so great this way. Remote's great until it's not. Yeah. So a couple couple questions. One, the cloud storage, we can set that all up, but is there, are there any limitations on like sizes or, I mean, 'cause we're hosting, I assume it's fine but there's also gonna be ingestion into the da Mongo database. So, and I and I, that's, there's no restrictions on that, right. Size wise. Okay, cool. And then I just wanted to confirm with you, we actually don't have the images for most of the ROIs and the reason we don't is because it's just so much, there's so many particles in the ocean and, and that's a lot of information for us to retain on these deployments. So we actually, on the instruments themselves, pull out the particles only occasionally save a full frame so we can't go back to the original at this time.

19:31 Sid Mehta
Got it, okay, good. No worries. Yeah, yeah, if you, if you have it, it's like we can make it work if you don't have it.

19:35 Danelle Cline
Yeah, we do have some, it would be interesting to explore that. Probably a different project but that's, that's of interest. This is kind of a great test case because it covers a lot of data. It covers rare classes, it covers, you know, looking, visualizing through embeddings and things that we've, we've really kind of been been able to do but more manually and, and our cycle partly is slow because we have to do run the processes ourselves. The tooling isn't all integrated. And we also work, we also work on many projects. I have five projects I actively work on so I don't have time to just focus on this particular one. So we have lots of bottlenecks in there, people, projects, you know, resource for resource bound. So this is really exciting.

20:28 Sid Mehta
Yeah, yeah, yeah. I think definitely some of the stuff that you're saying we can help you kind of streamline and automate as well.

20:33 Danelle Cline
Yeah, yeah. That discovery part, I don't think we should understate that like the discovery of like looking through the model results but also finding things that might be kind of rare and interesting. For example, you know, there are particular animals that divide so they might have a single cell and then dividing and those are the kinds of things that some of our colleagues have been able to see when they really look deep in the data. So those are the kinds of things that would be exciting to see come out of this.

21:05 Sid Mehta
Yeah We're, we definitely help a lot of teams find those needles in the haystacks, so Neat.

21:10 Danelle Cline
Very cool. Very cool.

21:11 Sid Mehta
Got Got it. Cool. B Breen, did you have a question that you wanted to ask?

21:16 Praveen Palem
Yeah, one question that Daniel stated early on, you said you had audio, video and images use cases. I was just curious potentially in the future, what do you, do you foresee using video and audio also in the tool?

21:32 Danelle Cline
I would love to see that capability in a unified tool, but I'm not the authority on that. We can make recommendations, but we do have a diverse set of data here. I can tell you that the tools, some of the tools we have work okay. But there's almost always some limitation because our data, even our video data varies from time lapse plankton time lapse to 4K 60 to 120 frames per second. And so it's really diverse and even how you visualize it and play and all of these things. So yeah, it's challenging, it's fun.

22:23 Praveen Palem
Yeah, for sure.

22:23 Laura Chrobak
That's just to say that we don't have any other types of data for this immediate project, but we can always, this institution operates a lot by recommendation and collaboration. So if it ends up being really a useful tool, we can definitely recommend other people to have that type of data to leverage it.

22:41 Praveen Palem
Yeah, that's, that's music to our ears. We do have video use cases a lot and also we're going into audio use cases with Apple for example. So you know, we'd love to explore that.

22:52 Danelle Cline
Oh, tell me more about that. Just curious.

22:55 Praveen Palem
Yeah, so one of the proof, proof of concepts working with Apple is they have, for example, they have a bunch of audio files and they input them all into the tool and they create embeddings from it and then they want to potentially search using an audio sample. Like you could literally take your phone outside and record a wind and then come back and say, okay, now go find me all of the wind samples. Yeah. Or or music one, one of the champion was saying they have a he heavy musician focused use case also where musicians wanna find like eighties guitar riff for example. And the tool should be able to bring back by text and audio.

23:45 Danelle Cline
Yeah, that's great. Very, very cool. Well we have a very large, I won't stay with this too long, this is not the purpose call, but we have a really large audio archive, which I've been working on for 10 years now. So we have a, an really interesting data set with some diverse sounds. Of course underwater sound is a whole different thing, but as we know, sound is all almost always converted to an image through spectrogram and that's where all the models work. So it makes perfect sense that you would find a tool that's image-based would work.

24:17 Laura Chrobak
They're doing a, like a whale related test in the test tank right now. So from where I sit I've been hearing whale audio Playing whale all day.

24:27 Danelle Cline
So I mean, yeah. Are you Laura, really? Yeah. Yeah. So cool. At any rate, I do wanna, it's such a cool thing to be able to do this. There are no tools that work well with audio at large scale, so it's really, really needed.

24:46 Praveen Palem
So I'm excited to hear that, that that's, That's, yeah actually you would be thrilled to know that we don't convert audio to spectrogram and treat it as an image classification. We, we actually process it using Clap for example, which is a audio embedding model. And so we, we actually process it as audio. Are you sure the model isn't converting it to a spectrogram in the model That I'm not a hundred percent sure but Clap is designed to be embeddings for audio, but I'm not the expert on that.

25:18 Danelle Cline
I'm, yeah, There's a lot of really interesting models. We've been trying a lot. Even Google, Google made a model I called, they call it their multi-species model and it doesn't work well on our data even though it's trained in domain. Oh it's just, it's just, it's yeah audio's, its a whole nother beast. So anyway, let's, let's continue with our focus here.

25:40 Sid Mehta
I just thank You for that but, but but it's a good call.

25:42 Danelle Cline
Yeah. I be a test driver for your audio tools.

25:46 Sid Mehta
Yeah, yeah it's a good call out and like as we kind of get the initial use case up and running and this, I think we can then also show like, you know, 'cause again you'll have access to the tool, you can bring in your video data, audio data at any other time. So yeah, that, that will always be an option. So we can kind of, once you're kind of ready to test that out, we can also like work for that out maybe after the first initial milestones that you guys have set. So. Cool. Sound good? So I think we're all good to understand where you guys are coming for and what, what what you're doing and what you're wanting to do with the tool. I think next thing is just like, so in terms of like communication, we do like meeting with our customers, you know, generally once a week, but then we also do offer support like Async as well. So if there's any questions that you guys might have while things are going, we can answer Async if it's super high priority. Sometimes we'll even jump on a call, you know, kind of really depends but like we do also, like, at least what generally happens is that we have like a, a weekly sync as you guys are getting up and running and then eventually you get bored of us and you're like, you know what? Or there's just not that much to talk about 'cause you're already onboarded. So we'll meet like every other week and then eventually it's like once a month. So whatever cadence we're, we're happy to meet, we generally do recommend it's good to meet a bit more frequent and then it just naturally kind of tapers off. So you know, we're, we're here to help but like in terms of like Slack, Microsoft Teams email, what would be the best way to set up like a nice communication channel?

27:08 Laura Chrobak
Slack.

27:09 Sid Mehta
Slack. Perfect. Okay. Big fan of Slack. Don't wanna tell you what I think about my customers who use Microsoft Teams and customers who use emails. They're like, they're on a list for me. So yeah, I love Slack so that's great. So Sounds good.

27:24 Azriel Nicdao
Feel free to set it up live this call. I was gonna wait until we got it Ping back but I think Dr. Rule just sent for signature. I moved the start date to the 10th in case I think BASC is his name, your guys' CFO is busy so, but don't worry about it. We'll have like three extra days of support.

27:43 Sid Mehta
Yes, I Got you. Yes. Okay. Alright, cool. Awesome. So, we'll I think Breen, you have their email name so you should be able to send them like a Slack invite and then we'll have a shared Slack channel that we can send that over to you guys so, perfect.

27:57 Danelle Cline
Yeah. So are, do you have any recommendations that of what we could be doing to better familiar familiarize with the tool in terms of, I don't know, just I, you know, single users stand up a an instance That's a good segue to moving to the enterprise version. I mean we can, I can do the, I did the loading exercise that was sort of like, okay I checked that.

28:24 Sid Mehta
Yeah, Yeah.

28:25 Danelle Cline
Is There anything else that you can think of?

28:27 Sid Mehta
Yeah, I think we'll walk you through it. 'cause I think there's like some bells and whistles in the enterprise. Like we, we, we talk, we, there's like some stuff that you can just point and click in the ui. So we'll once we give you deployment we'll kind of do a nice walkthrough of like, hey, now that you have this deployment, what else is there? 'cause there's also concept, I think maybe AZ talked to you about, like for example the embeddings, you can run it into SDK that's fine. But then you can also, you'll, you can also run it into the UI and if you run it into UI you'll wanna schedule the operation as well because it, you know, it can take a while, right? Especially for the amount of data that you guys are going. So we'll kind of walk you through those. But I think like it sounds like you have a good grasp of like, you know, label types in 51, how to create samples. Like I think, you know, some customers are are walking in code like that. So the fact that you have a good exam, I strong goal to 51 is great and then 51 enterprises on Pravin and I are gonna make you show what else you can do with the, with the tool as well.

29:17 Danelle Cline
So I think you're, Is that scheduling done? Is that scheduling because, because it takes a long time to run. Is it a CPU or a GPU?

29:26 Sid Mehta
So 'cause so yeah, we'll talk about info but you guys are on, we'll we'll be managing the info on you. So for you, but it will be on historically all of our managed customers have had access for CPUs for this type of delegate delegated operation. But we are actually announcing very soon potentially GPU access as well. So if customers want to opt in, but it'll be a little down the road. I think AZ will will have to have a conversation in turn some more internal conversations on, on that because it might just be a slight upcharge. But, but yeah, we, but yeah, so there is a, a nice CPU system as well, but then for customers who want to go faster, there will be an option I think down the road to, to use GPU and we'll walk that over through. Okay. It's already, it's coming in the next release.

30:12 Danelle Cline
So it's, I'm I'm about that because that that is certainly a big Yeah, yeah. Performance difference and Right, right.

30:20 Sid Mehta
Yeah but like locally, like if you run this on the SDK and the local system that you're running, the SDK on has access to A GPU that also, you know, can work. So it, yeah, it depends. So we wanna give customers the option to use our compute, but if you know you have your compute as well, that works. So yeah, so we'll walk you through that. So actually that's a good segue to my next set of questions, which are just on infrastructure. So the biggest thing that we need from you, so first of all, I think you made the best decision of your life going with manage. So it's great. You don't have to worry about the database, you don't have to worry about anything upgrades. We'll do that all for you. The only thing we'll need for you is just the identity provider. So how they, for SSO, so how like people in your organization can sign in. So we use zero for that. So it's usually the usual culprits for this are something like Okta, Azure, AD saml, OIDC, Google Workspaces. Do you know, do you know what that would be for you guys? Oh, I think for some reason we can't hear you.

31:22 Danelle Cline
I'm sorry. It was my understanding we were gonna do social account logins and not use our company SSO because we have external people they're using the tool and internal people.

31:31 Sid Mehta
Yeah.

31:32 Danelle Cline
So this is a little bit out of my domain.

31:35 Azriel Nicdao
So Yeah, you might have to sync with Alan about like the other setup that we had mentioned Syd, but okay. There's like a thread in via Aloha channel about it.

31:45 Sid Mehta
Yeah.

31:46 Danelle Cline
Okay. So do we have an SSO internally Got it. That that's only gonna cover, you know, us that are external collaborators that won't work. We don't, they don't have company accounts. So we have a people at some universities that are gonna be contributing.

32:00 Sid Mehta
Got It, okay. Yeah, I guess even for that social account, it would have to be, I, I assume in one of those one's AZ, like OIDC or whatnot, so Yeah. Got it.

32:10 Azriel Nicdao
Yeah, I Think it was, I think we had talked about like this specific team on this project spinning up like an auth zero account and then you'd be getting like that IDP information for, for them to do like shareable logins with social logins for the pe the external collaborators that they work with.

32:29 Sid Mehta
Got it. Okay. So do you know, I guess how, who, who would set that up on your side? Is that, or how long it would take for them to set that up? 'cause I think that's, that would be a requirement for us to get the deployment up and running. So you guys, like we can get the deployment up and running on our end, but then how would we plug into your kind of SSO is kind of like a, a piece that we would need to spin up the deployment.

32:59 Danelle Cline
Yeah, I don't know. Okay. We're, we're, we're really hoping that we wouldn't have to involve our IS department in this decision, so.

33:08 Sid Mehta
Got it. Yeah, if you have someone who has like SSO knowledge I can that you can like introduce me to, we can add into the Slack channel and I can also go back and forth with them that that can also work as well.

33:21 Danelle Cline
Well if you could Tell me, I think I, I think I know somebody that could get you started, but what, what exactly is it that you need?

33:28 Sid Mehta
Yeah, so generally what happens set Up? Yeah, so generally what happens is that for odd zero we, we have like, it's either Okta, Azure, saml, OIDC and what we'll give you for being, we'll create like a tenant on our end, we'll give you a callback URL and then once you give them a callback, once we give you the callback URL, you give us some types of IDs and secrets, which are for your, for your IDP. And once we have those secrets, that's this client ID and secret, that's all we need then to like do authentication with your, with your SSO.

34:09 Danelle Cline
But that's just our SSO. But if our collaborators aren't on our SSO, they have, there's a separate path for them to do like Google authentication or can we, can we just make it all Google Auth?

34:26 Sid Mehta
Yeah, I think it could all be Google auth. It, it is just either they, we will have to see whether you want to use one that's internal, like internal only and you add them to their internal or we use a Google auth that like both internal and external have access to. So yeah, if it's Google Auth then you know, that would be helpful for us and we would send someone a callback URL and they would just give us the secrets for Google, for Google authentication, the client ID and secrets Because we have, if we log in with our, let's say I go to, to my Chrome browser and I wanna log into my Google drive.

35:00 Danelle Cline
Yeah. I can log in with my company account Got it. With my company email. It all just works and that connects. So I don't necessarily have to set anything up in that regard. Yeah. So I'm, I'm, I'm a little confused why, why we need to give you secrets and what, why that's necessary.

35:24 Sid Mehta
It's just for the, it's called like a client idea or secret. So basically it's like your SSO is just telling like that it's your single sign on is saying it's okay to use this, your, your SSO for this, it it, I think it's like a perfect Oh, I Gotcha.

35:39 Danelle Cline
Okay. So it allows us to use use this app Yeah.

35:44 Sid Mehta
To log in To to log in. Yeah. Yeah, yeah. And maybe I can kind of show you on my end what it'll look like, but Clearly I don't understand this domain and that's fine.

35:54 Danelle Cline
I don't really wanna know this.

35:56 Sid Mehta
Yeah, I know, I know, I know, I know. When I say the words client ID and secret sound really like, oh my God, what are we sharing?

36:01 Danelle Cline
You know, I had, I tried to go down this for an app once. Yeah. And I just, it hurt my, hit my head so much and I was like, oh my gosh, the, the whole exchange call back thing is Yeah. Yeah. It was really, it just seemed unnecessarily.

36:12 Sid Mehta
Yeah. Yeah, I agree. I, I'm a hundred percent with you. ML stuff is so much more easy, but it's basically making sure that you can do this. Okay. And then on my end, let's see, it'll show up here, but like it should show up. Maybe it's cashed or not, but it'll, it should show up that you can let log, I can log in with my Google cloud account. So, okay. It just worked automatically so it wasn't as useful, but Okay. It sounds like you guys might be using Google thing, but it would just be good to verify.

36:39 Danelle Cline
So basically what, what we use, I dunno what we're using, but I can ask the IS department Got it. And find out who that point of contact would be and Yeah, yeah, we can Get that connected to you.

36:53 Sid Mehta
Perfect. Yeah. Yeah. So we'll just need that client ID in secret and then once you give us that, then that's all we need then to split spin up your deployment. We'll, so yeah, once we have that, it's like actually like pretty quick on our end, like in one or two days. So that's like the only thing. So call back you rl, you'll send, you'll give us the ID in secret and then we'll you'll have a deployment that you can log into. And then the only thing that we'll need then is that when you log into the deployment, like how I did there, you'll initially log in as like a guest, but then we will need to, like the first person who logs in will just promote you to admin and then that admin then can invite Okay. Everyone else. So who, who would be a good candidate to, for that first invite for the admin?

37:32 Danelle Cline
Ooh mm. Another I admin can promote other people, right?

37:38 Sid Mehta
Admin. Yeah, yeah, yeah, yeah, yeah. So yeah, if we give Laura the Kings, Kings to the kingdom so she can like, you know, upgrade you to admin as well. So yeah, it's just that initial one, so. Okay, cool. So sounds like we have the right people on the call for that, so great. Yeah. And then after that I can kind of share with you this, then after that it's like we have, that's like, I think the first milestone is being able to log in and then the second milestone is probably what we, what we work with customers is then to like visualize their, their data set in 51 enterprise. And we have a whole thing in our docs for that. And we'll, and no worry, you don't have to note this down, we'll put it all on a Slack channel, but we have in our docs a whole like getting started with 51 enterprise section, which is then what we would recommend you guys to go through. So it'd be co configuring those cloud credentials on your deployment, putting in those ad AWS credentials and then just walking through this kind of tutorial on like setting up your API keys and then how to like load a data set. So that would be kind of, I think the second milestone we should aim for.

38:40 Danelle Cline
And, and just to clarify, so this, this is great. I I I think it's great you have great documentation. If I have another, let's say I wanna grow this deployment still, if I understand it, it's still tied to one set of keys in one Amazon account. So I can't have multiple accounts in multiple buckets.

39:05 Sid Mehta
That's a good question. I actually went through this. I believe you can, sorry, my camera's going outta focus. I'm still focusing, but I think I, I did believe you can have multiple AWS buckets. I'll double check on that. I had a customer ask me this with Azure and he was able to upload two credentials To it.

39:24 Danelle Cline
Okay. It's just a minor thing, but it could be a point of confusion. Got it. We have data in different accounts and you know, we can make things public, but some people don't wanna do that kind Of thing.

39:33 Sid Mehta
Got it, got it. Yeah. Yeah, I think you can, I'll, I'll double check on that or once we cross that bridge, but I believe you can.

39:39 Danelle Cline
So yeah, But initially we'll just have an an A single account and that that's tied to this setup and Laura will get the keys to the kingdom and Yeah, Once logging in as a guest and then, but before any of this happens, you need to, to have the keys and the secret, the client IDs and the secrets. And you're gonna give me a call back, IURL for the is.

40:05 Sid Mehta
Yeah.

40:05 Danelle Cline
And, and that's all that's gonna happen. Okay.

40:08 Sid Mehta
Yeah, You sound like a security expert already, so Yeah, don't worry. We'll, we'll also, yeah, Pravin and I will put this all in the Slack message as well. We'll we'll put the Slack thing in the URO and then also ask what we're looking for back. So you know, it's all there so don't worry about writing it down. But yeah, that's basically what we'll need. And then, yeah, and then, yeah, I think that's what we're working for. I think those would be the first two milestones. And then once you have that, that's like a good san the, this, what I have in the docs here is a good sanity check that like everything works. You can see your cloud data and then you're basically then, you know, then I think that's like a good time to then start focusing on like the timelines and, and you know what you want to go.

40:42 Danelle Cline
So yeah. And only one set of keys. There's not, there's only one API key, is that correct?

40:49 Sid Mehta
Oh, it's API I key per user. So you'll have your own API key and then Laura will have her own.

40:53 Danelle Cline
Okay. Yeah.

40:55 Sid Mehta
Okay, makes Sense. Cool. Any questions there? I guess the main thing and then, yeah, like I said, we do recommend setting up some type of weekly syncs, but I guess it makes more sense. I think the next step would be probably to weekly sync once we have the deployment up and running. So we can also walk you through it and then answer any questions that you have going through this next step. But like in general, do you have an idea of like, what's a good time for you to, to like meet and discuss?

41:22 Danelle Cline
For me, Thursdays and Fridays are always good. Wes Wednesdays never work for me. And Mondays is not a good, it's Monday.

41:30 Sid Mehta
Yeah, It's Monday, right?

41:32 Danelle Cline
Yeah, yeah, it can be. But Thursdays or Fridays okay. Are generally better for me. And my schedule's pretty wide, fairly wide open.

41:40 Sid Mehta
Okay. L Laura, does Thursdays work for you as well?

41:43 Laura Chrobak
Thursdays would be great.

41:44 Sid Mehta
Okay. Yeah, Pravin. Okay, sounds good. So I think Pravin can also send like some times over of like when we would want to schedule those up. We can put one on for next Thursday and I think, I hope with everything that we should have something to chat about with it, with the deployment up and running, but just in case we don't, worst case we cancel it and you know, or we meet another day, so no worries. So, okay, cool.

42:04 Laura Chrobak
We'll also send an invite for us to meet next Thursday just to, and then from here on now as well until we wanna change the cadence Just to reiterate, but beyond Henry signing the doc that we need next week and then getting you all the secret client information that you need to move forward with creating admins, is this step also something you wanted us to do, the one you're showing right now before Thursday? Or is that something that we would do then?

42:46 Sid Mehta
The getting our data into the, Yeah, I mean your call, it's, if you, if you have access, I'm assuming everything goes well, you have access, I think it would be great to just, you know, try it out that way if you run any hiccups or there's anything that we can debug, we can debug live on the call. So if you can try it out beforehand, that'd be great, but if not, we could also use that call to like walk through it, the deployment. So, you know, I think, yeah, if you look at it and then you have come with some questions like, hey, this didn't make sense, that would also be great as well. You know, we're always trying to improve our documentation, so if it's not intuitive in documentation, then we have work to do.

43:21 Danelle Cline
So Sid, are you the point of contact for the authentication?

43:25 Sid Mehta
Can I Yeah, yeah. If you just tag me or Pravin on it, both of us, I think that'll be fine for now. But yeah, if they, if they need like any more questions or anything of that, yeah, do let, yeah, just let both of us know.

43:36 Danelle Cline
I imagine they're gonna wanna have it like, because they're sharing keys, they'll wanna have, they'll be some, yeah. Some security concerns about how that's done. Got it. Okay. Yeah, we have a a, what is that title? He's like a security expert here.

43:57 Sid Mehta
Okay. If that's the case that they need one person and one person only, then yeah, you can put Pravin s name. Okay. That he'd probably be the one who's gonna be, he's gonna be sending it all that up so he, he's gonna be the one needing it.

44:06 Danelle Cline
Pravin, What's your email?

44:11 Sid Mehta
Oh, I think you're on mute. Pravin?

44:14 Praveen Palem
Yeah, it's Pravin at walks up com.

44:17 Danelle Cline
Oh, that's easy.

44:19 Sid Mehta
Yeah.

44:20 Danelle Cline
Okay. But we don't have an account yet, right? We're still waiting for the paperwork.

44:27 Sid Mehta
Oh, is that are, are you asking this?

44:29 Danelle Cline
It's a question. We don't have an account account number yet. Account number, Do we? Yeah, like we have, we signed a contract.

44:38 Azriel Nicdao
We can hear That. Yeah, we have one on the order form. I can, I can send it over to you. Okay. Lemme see. I'm like sending something to facility right now.

44:47 Danelle Cline
Oh good. Just put in the chat really quick.

45:01 Azriel Nicdao
This is, I think it should be this. Okay.

45:19 Danelle Cline
Okay. Oh, that's easy.

45:26 Sid Mehta
Oh, and then I, I guess one question I forgot to ask for this SSO stuff, we do also have to choose a region when we create your tenant. It's like us, Europe, Asia, Americas, I assume it'd just be us. Yes. Yeah. Okay, perfect.

45:42 Danelle Cline
What does that mean?

45:45 Sid Mehta
It's, it's, again, I'll be honest, s SSO stuff that like I wish I was an expert on, but I'm not.

45:50 Danelle Cline
But I think it's Just like, it's, it's related to that.

45:51 Sid Mehta
Okay. Yeah, it's like related to where you're signing in from and what region the tenant needs to be in for authentications, something like that. Yeah, I know, you know, people say young people say, I'm not a rapper, that's, I wanna say that, but I'm not, I'm not an, I'm not a security guy. That's what I want to say. So I have, I have also, you know, very limited knowledge of of it, but, Well we don't either.

46:12 Danelle Cline
And we were happy that we hired somebody who's a senior information system. Security guy.

46:18 Laura Chrobak
Yeah, administrator. Okay. Person, people Person.

46:21 Danelle Cline
I'm sorry. Yes. Administrator. Yes, person. Thank you. Thank you. And we just got an email from our senior security administrator that there's a vulnerability in the React server components. So if you have React, you use it in your web app, you might wanna check. Oh, okay. Yeah. Makes sense.

46:43 Sid Mehta
Yeah. All right, cool. Anything else? Any questions you guys? I think we're aligned on next steps. So I think a lot of this stuff will kind of just reiterate in the Slack channel, but anything else that comes to mind at this time?

46:56 Laura Chrobak
Really quickly, I was just gonna ask, there are in the getting started page, are there any other particular spots you would direct us to from the, the 51 enterprise subsets that you think would be worth looking into? I'm sure I can poke around myself, but if you're like, this is key Me.

47:21 Sid Mehta
That's a good question. I feel like at the time being like that would be 'cause like I don't think you getting started. Yeah, I think at the getting started and just like understanding those steps, steps would probably be that. 'cause then yeah, once that's all said and done, then it's like you, you, most of the times what happens is that you do that step and then you never have to do it again. And then after that I think it, it makes a lot of sense to then talk about, I think once we do have a deployment, we do wanna walk you kind of through the concept of dos and how you can run your own embeddings operations. So some of those stuff we would like to do that, but yeah, I'll have to see if whether we're, what's a, what's a good place for us to go. But I think that's like the main thing that you would want to kind of look at in the enterprise one for now.

48:01 Laura Chrobak
Okay. Yeah. And then I guess Danelle, we should also work on getting the S3 bucket ready for Yes.

48:10 Danelle Cline
And that, that's, that's gonna be, yeah, we're gonna have to alert Henry to that. There'll be some cost, it won't be very much, but there'll be a little cost associated with that.

48:22 Sid Mehta
Yeah, if, if you could, that would be great. 'cause like, yeah, just to show you on the, on the example that we have, so we do have like the AWS examples. So it is like, I'm gonna ask in this example to list like a bucket URL and it kind of assumes that it does have images. So yeah, that could be like one thing in parallel while we're working on getting your deployment running, if you have that ready, then like once your deployment is up and running you can really, you can quickly test all this type of Stuff.

48:47 Danelle Cline
Yeah. But, and if I understand it, just to, to be clear, we set up a bucket and we have some credentials and it's a single set of credentials for the single instance.

48:58 Sid Mehta
Yeah. For the entire deployment. Yep. So every user, yeah, yeah. So every user who will log into deployment is, is gonna have Access to the credentials.

49:07 Danelle Cline
Right. And mostly it's read, but in the cases that it's w right, we won't know who, who made that change, which is probably fine for any everything we're doing, but just so we understand.

49:19 Sid Mehta
Yeah, I think Wright can also be sometimes somewhere, sometimes we're W right, is helpful is like sometimes if you ever have data locally, like let's say if you have data locally on your image on your laptop and then you want to go through 51 to like, actually we also provide the ability to write to buckets as well with our SDK. So sometimes what people do is they'll upload media and then they'll upload it. It won't show in 51 Enterprise 'cause it has a local file path, but then you can update the file paths and write it to the bucket as well. So we also, so some, so that's also another use case where write might be useful.

49:51 Danelle Cline
Yeah. Okay.

49:52 Sid Mehta
That's good to know. Yeah. Yeah. So other than that, and yeah, anyone who uses videos also generally needs right access because if, a lot of times people work in videos but then they wanna work on frames and then for frames we do need to kind of write images into the bucket to view the frames.

50:08 Danelle Cline
So Yeah. Good.

50:10 Sid Mehta
Awesome. Cool. Yeah, no, all good questions and yeah, sounds good. All right, well you know it's Friday. I don't wanna keep anyone longer than, than we need to be. So if nothing else then have a great weekend everybody.

50:25 Laura Chrobak
Thank you. Thank you, you.

50:29 Azriel Nicdao
Bye everyone.

50:31 Laura Chrobak
Bye.

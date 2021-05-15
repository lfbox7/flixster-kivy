# Flixster_Python_Kivy

Flixster is an app that allows users to browse movies from the The Movie Database API.
This was an experimental project using Python's Kivy module to create both an Android and iOS app.

Time spent: **16** hours spent in total

### User Stories

- [x] User can view a list of movies (title, poster image, and overview) currently playing in theaters from the Movie Database API.

### App Walkthough GIF
Here's a walkthrough of implemented user stories:

<img src='http://g.recordit.co/SPX4wMgnBO.gif' width=350>

GIF created with [RecordIt](http://recordit.co/E0HkXA7DLF).

### Notes
There were many challenges faced trying to implement this app with Python's Kivy module. First and foremost was trying to create a dynamic .kv file. Bring the API into Python was easy, but parsing to the data to the views was challenging as this module is outdated and has a very small community supporting it. Because this module is outdated, it was impossible to push the Android and iOS apps to their respective simulators as Kivy required both an Android Studio and Xcode that was four or five versions behind current builds making it impossible to open the app in either simulator.

I am not a proponent of non-native builds for mobile, but I thought I would give this one a try since I was learning Python. It was however a huge disappointment and I would recommend others to stick to native builds.

### License

Copyright 2021 Leonard Box

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.



# The New Python Print Function

**The New Python Print Function** is a Python library that extends the functionality of the built-in `print` function by adding support for specifying foreground colors, background colors, and font styles directly. These features are implemented internally using ANSI escape sequences.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
  - [Supported Colors](#supported-colors)
  - [Supported Font Styles](#supported-font-styles)
- [Contributing](#contributing)
- [License](#license)
- [Author](#author)

## Installation

Install the package using `pip`:

```bash
pip install nprint
```

Or:

```bash
python3 -m pip install nprint
```

---

## Usage

Here’s how you can use the `nprint` function:

```python
import nprint

# Print regular text
nprint("Hello, world!")

# Print text with a red foreground
nprint("Hello, world!", fg="red")

# Print text with a yellow background
nprint("Hello, world!", bg="yellow")

# Print bold text
nprint("Hello, world!", fs="bold")

# Combine options: red foreground, yellow background, bold font
nprint("Hello, world!", fg="red", bg="yellow", fs="bold")
```

### Function Signature

The `nprint` function signature is as follows:

```python
nprint(*objects, sep=' ', end='\n', file=None, flush=False, fg=None, bg=None, fs=None)
```

- **`fg`**: Specifies the foreground color.
- **`bg`**: Specifies the background color.
- **`fs`**: Specifies the font style.

---

## Features

- **Extended `print` functionality**: Maintain all capabilities of the standard `print` function with added color and style options.
- **141 Colors Supported**: Apply any HTML-supported color to text or background.
- **11 Font Styles**: Customize the appearance of your text with various font styles.
- **Developer-Friendly**: Auto-completion support for IDEs simplifies usage by listing available options.

### Supported Colors

The color names are derived from valid HTML color names, ensuring a familiar and intuitive experience.

#### Blues

1. <p style="background-color: cyan; color: black;">cyan</p>
2. <p style="background-color: aqua; color: black;">aqua</p>
3. <p style="background-color: lightcyan; color: black;">light-cyan</p>
4. <p style="background-color: paleturquoise; color: black;">pale-turquoise</p>
5. <p style="background-color: aquamarine; color: black;">aquamarine</p>
6. <p style="background-color: turquoise; color: black;">turquoise</p>
7. <p style="background-color: mediumturquoise; color: black;">medium-turquoise</p>
8. <p style="background-color: darkturquoise; color: black;">dark-turquoise</p>
9. <p style="background-color: cadetblue; color: black;">cadet-blue</p>
10. <p style="background-color: steelblue; color: black;">steel-blue</p>
11. <p style="background-color: lightsteelblue; color: black;">light-steel-blue</p>
12. <p style="background-color: powderblue; color: black;">powder-blue</p>
13. <p style="background-color: lightblue; color: black;">light-blue</p>
14. <p style="background-color: skyblue; color: black;">sky-blue</p>
15. <p style="background-color: lightskyblue; color: black;">light-sky-blue</p>
16. <p style="background-color: deepskyblue; color: black;">deep-sky-blue</p>
17. <p style="background-color: dodgerblue; color: black;">dodger-blue</p>
18. <p style="background-color: cornflowerblue; color: black;">cornflower-blue</p>
19. <p style="background-color: mediumslateblue; color: black;">medium-slate-blue</p>
20. <p style="background-color: royalblue; color: black;">royal-blue</p>
21. <p style="background-color: blue; color: black;">blue</p>
22. <p style="background-color: mediumblue; color: black;">medium-blue</p>
23. <p style="background-color: darkblue; color: black;">dark-blue</p>
24. <p style="background-color: navy; color: black;">navy</p>
25. <p style="background-color: midnightblue; color: black;">midnight-blue</p>

#### Browns
26. <p style="background-color: cornsilk; color: black;">cornsilk</p>
27. <p style="background-color: blanchedalmond; color: black;">blanched-almond</p>
28. <p style="background-color: bisque; color: black;">bisque</p>
29. <p style="background-color: navajowhite; color: black;">navajo-white</p>
30. <p style="background-color: wheat; color: black;">wheat</p>
31. <p style="background-color: burlywood; color: black;">burly-wood</p>
32. <p style="background-color: tan; color: black;">tan</p>
33. <p style="background-color: rosybrown; color: black;">rosy-brown</p>
34. <p style="background-color: sandybrown; color: black;">sandy-brown</p>
35. <p style="background-color: goldenrod; color: black;">goldenrod</p>
36. <p style="background-color: darkgoldenrod; color: black;">dark-goldenrod</p>
37. <p style="background-color: peru; color: black;">peru</p>
38. <p style="background-color: chocolate; color: black;">chocolate</p>
39. <p style="background-color: saddlebrown; color: black;">saddle-brown</p>
40. <p style="background-color: sienna; color: black;">sienna</p>
41. <p style="background-color: maroon; color: black;">maroon</p>
42. <p style="background-color: brown; color: black;">brown</p>

#### Greens
43. <p style="background-color: greenyellow; color: black;">green-yellow</p>
44. <p style="background-color: chartreuse; color: black;">chartreuse</p>
45. <p style="background-color: lawngreen; color: black;">lawn-green</p>
46. <p style="background-color: lime; color: black;">lime</p>
47. <p style="background-color: limegreen; color: black;">lime-green</p>
48. <p style="background-color: palegreen; color: black;">pale-green</p>
49. <p style="background-color: lightgreen; color: black;">light-green</p>
50. <p style="background-color: mediumspringgreen; color: black;">medium-spring-green</p>
51. <p style="background-color: springgreen; color: black;">spring-green</p>
52. <p style="background-color: mediumseagreen; color: black;">medium-sea-green</p>
53. <p style="background-color: seagreen; color: black;">sea-green</p>
54. <p style="background-color: forestgreen; color: black;">forest-green</p>
55. <p style="background-color: green; color: black;">green</p>
56. <p style="background-color: darkgreen; color: black;">dark-green</p>
57. <p style="background-color: yellowgreen; color: black;">yellow-green</p>
58. <p style="background-color: olivedrab; color: black;">olive-drab</p>
59. <p style="background-color: olive; color: black;">olive</p>
60. <p style="background-color: darkolivegreen; color: black;">dark-olive-green</p>
61. <p style="background-color: mediumaquamarine; color: black;">medium-aquamarine</p>
62. <p style="background-color: darkseagreen; color: black;">dark-sea-green</p>
63. <p style="background-color: lightseagreen; color: black;">light-sea-green</p>
64. <p style="background-color: darkcyan; color: black;">dark-cyan</p>
65. <p style="background-color: teal; color: black;">teal</p>

#### Greys
66. <p style="background-color: gainsboro; color: black;">gainsboro</p>
67. <p style="background-color: lightgrey; color: black;">light-grey</p>
68. <p style="background-color: silver; color: black;">silver</p>
69. <p style="background-color: darkgrey; color: black;">dark-grey</p>
70. <p style="background-color: grey; color: black;">grey</p>
71. <p style="background-color: dimgrey; color: black;">dim-grey</p>
72. <p style="background-color: lightslategrey; color: black;">light-slate-grey</p>
73. <p style="background-color: slategrey; color: black;">slate-grey</p>
74. <p style="background-color: darkslategrey; color: black;">dark-slate-grey</p>
75. <p style="background-color: black; color: white;">black</p>

#### Oranges
76. <p style="background-color: lightsalmon; color: black;">light-salmon</p>
77. <p style="background-color: coral; color: black;">coral</p>
78. <p style="background-color: tomato; color: black;">tomato</p>
79. <p style="background-color: orangered; color: black;">orange-red</p>
80. <p style="background-color: darkorange; color: black;">dark-orange</p>
81. <p style="background-color: orange; color: black;">orange</p>

#### Pinks
82. <p style="background-color: pink; color: black;">pink</p>
83. <p style="background-color: lightpink; color: black;">light-pink</p>
84. <p style="background-color: hotpink; color: black;">hot-pink</p>
85. <p style="background-color: deeppink; color: black;">deep-pink</p>
86. <p style="background-color: mediumvioletred; color: black;">medium-violet-red</p>
87. <p style="background-color: palevioletred; color: black;">pale-violet-red</p>

#### Purples
88. <p style="background-color: lavender; color: black;">lavender</p>
89. <p style="background-color: thistle; color: black;">thistle</p>
90. <p style="background-color: plum; color: black;">plum</p>
91. <p style="background-color: violet; color: black;">violet</p>
92. <p style="background-color: orchid; color: black;">orchid</p>
93. <p style="background-color: magenta; color: black;">magenta</p>
94. <p style="background-color: mediumorchid; color: black;">medium-orchid</p>
95. <p style="background-color: mediumpurple; color: black;">medium-purple</p>
96. <p style="background-color: blueviolet; color: black;">blue-violet</p>
97. <p style="background-color: darkviolet; color: black;">dark-violet</p>
98. <p style="background-color: darkorchid; color: black;">dark-orchid</p>
99. <p style="background-color: darkmagenta; color: black;">dark-magenta</p>
100. <p style="background-color: purple; color: black;">purple</p>
101. <p style="background-color: rebeccapurple; color: black;">rebecca-purple</p>
102. <p style="background-color: indigo; color: black;">indigo</p>
103. <p style="background-color: slateblue; color: black;">slate-blue</p>
104. <p style="background-color: darkslateblue; color: black;">dark-slate-blue</p>

#### Reds
105. <p style="background-color: indianred; color: black;">indian-red</p>
106. <p style="background-color: lightcoral; color: black;">light-coral</p>
107. <p style="background-color: salmon; color: black;">salmon</p>
108. <p style="background-color: darksalmon; color: black;">dark-salmon</p>
109. <p style="background-color: lightsalmon; color: black;">light-salmon</p>
110. <p style="background-color: crimson; color: black;">crimson</p>
111. <p style="background-color: red; color: black;">red</p>
112. <p style="background-color: firebrick; color: black;">fire-brick</p>
113. <p style="background-color: darkred; color: black;">dark-red</p>

#### Whites
114. <p style="background-color: white; color: black;">white</p>
115. <p style="background-color: snow; color: black;">snow</p>
116. <p style="background-color: honeydew; color: black;">honeydew</p>
117. <p style="background-color: mintcream; color: black;">mint-cream</p>
118. <p style="background-color: azure; color: black;">azure</p>
119. <p style="background-color: aliceblue; color: black;">alice-blue</p>
120. <p style="background-color: ghostwhite; color: black;">ghost-white</p>
121. <p style="background-color: whitesmoke; color: black;">white-smoke</p>
122. <p style="background-color: seashell; color: black;">seashell</p>
123. <p style="background-color: beige; color: black;">beige</p>
124. <p style="background-color: oldlace; color: black;">old-lace</p>
125. <p style="background-color: floralwhite; color: black;">floral-white</p>
126. <p style="background-color: ivory; color: black;">ivory</p>
127. <p style="background-color: antiquewhite; color: black;">antique-white</p>
128. <p style="background-color: linen; color: black;">linen</p>
129. <p style="background-color: lavenderblush; color: black;">lavender-blush</p>
130. <p style="background-color: mistyrose; color: black;">misty-rose</p>

#### Yellows
131. <p style="background-color: gold; color: black;">gold</p>
132. <p style="background-color: yellow; color: black;">yellow</p>
133. <p style="background-color: lightyellow; color: black;">light-yellow</p>
134. <p style="background-color: lemonchiffon; color: black;">lemon-chiffon</p>
135. <p style="background-color: lightgoldenrodyellow; color: black;">light-goldenrod-yellow</p>
136. <p style="background-color: papayawhip; color: black;">papaya-whip</p>
137. <p style="background-color: moccasin; color: black;">moccasin</p>
138. <p style="background-color: peachpuff; color: black;">peach-puff</p>
139. <p style="background-color: palegoldenrod; color: black;">pale-goldenrod</p>
140. <p style="background-color: khaki; color: black;">khaki</p>
141. <p style="background-color: darkkhaki; color: black;">dark-khaki</p>

### Supported Font Styles
1. <p style="font-weight: bold;">bold</p>
2. <p style="opacity: 0.5;">dim</p>
3. <p><i>italic</i></p>
4. <p><u>underline</u></p>
5. <p style="opacity: 0.78;">dim</p>
6. <p style="background-color: black; color:white; display: inline-block;">&nbsp;inverse&nbsp;</p>
7. <p style="opacity: 0.1;">hidden</p>
8. <p style="text-decoration: line-through;">strikethrough</p>
9. <p style="text-decoration: underline double;">double-underline</p>
10. <p style="border: solid black 1px; display: inline-block;">&nbsp;frame&nbsp;</p>
11. <p style="text-decoration: overline;">overline</p>

---

## Contributing

We welcome contributions! To contribute:

1. Fork the repository.
2. Create a new branch for your feature or fix.
3. Commit and push your changes.
4. Open a pull request.

For significant changes, please open an issue first to discuss your proposal.

---

## License

**Copyright** (c) 2024 Haripo Wesley T.\
**Email**: haripowesleyt@proton.me\
**GitHub**: https://github.com/haripowesleyt

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

1. The above copyright notice and this permission notice shall be included in all
   copies or substantial portions of the Software.

2. THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
   IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
   FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
   AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
   LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
   OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
   SOFTWARE.

---

## Author

- **Haripo Wesley T.**
  - **Email**: [haripowesleyt@proton.me](mailto:haripowesleyt@proton.me)
  - **GitHub**: [haripowesleyt](https://github.com/haripowesleyt)

---

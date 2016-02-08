<!DOCTYPE html>
<!-- Server: sfn-web-15 -->


  












<!--[if lt IE 7 ]> <html lang="en" class="no-js ie6"> <![endif]-->
<!--[if IE 7 ]>    <html lang="en" class="no-js ie7"> <![endif]-->
<!--[if IE 8 ]>    <html lang="en" class="no-js ie8"> <![endif]-->
<!--[if IE 9 ]>    <html lang="en" class="no-js ie9"> <![endif]-->
<!--[if (gt IE 9)|!(IE)]>--> <html lang="en" class="no-js"> <!--<![endif]-->
  <head>
    <meta content="text/html; charset=UTF-8" http-equiv="content-type"/>
    <title>
  Python Serial Port Extension / Code /
  [r508]
  /trunk/pyserial/examples/wxTerminal.py
</title>
    
<meta id="project_name" name="project_name" content='pyserial' />
<script src="http://a.fsdn.com/allura/nf/1433526507/_ew_/theme/sftheme/js/sftheme/modernizr.custom.90514.js"></script>
<!--[if lt IE 7 ]>
  <script src="http://a.fsdn.com/allura/nf/1433526507/_ew_/theme/sftheme/js/sftheme/dd_belatedpng.js"></script>
  <script> DD_belatedPNG.fix('img, .png_bg'); //fix any <img> or .png_bg background-images </script>
<![endif]-->
<link href='//fonts.googleapis.com/css?family=Ubuntu:regular' rel='stylesheet' type='text/css'>
<style type="text/css">
    @font-face {
        font-family: "Pictos";
        src: url('http://a.fsdn.com/allura/nf/1433526507/_ew_/theme/sftheme/css/fonts/sftheme/pictos-web.eot');
        src: local("☺"), url('http://a.fsdn.com/allura/nf/1433526507/_ew_/theme/sftheme/css/fonts/sftheme/pictos-web.woff') format('woff'), url('http://a.fsdn.com/allura/nf/1433526507/_ew_/theme/sftheme/css/fonts/sftheme/pictos-web.ttf') format('truetype'), url('http://a.fsdn.com/allura/nf/1433526507/_ew_/theme/sftheme/css/fonts/sftheme/pictos-web.svg') format('svg');
    }
</style>
    <script type="text/javascript">
            /*jslint onevar: false, nomen: false, evil: true, css: true, plusplus: false, white: false, forin: true, on: true, immed: false */
            /*global confirm, alert, unescape, window, jQuery, $, net, COMSCORE */
    </script>
    
      <!-- ew:head_css -->

    
      <link rel="stylesheet"
                type="text/css"
                href="http://a.fsdn.com/allura/nf/1433526507/_ew_/_slim/css?href=allura%2Fcss%2Fforge%2Fhilite.css"
                >
    
      <link rel="stylesheet"
                type="text/css"
                href="/nf/tool_icon_css?1433526507"
                >
    
      <link rel="stylesheet"
                type="text/css"
                href="http://a.fsdn.com/allura/nf/1433526507/_ew_/theme/sftheme/css/forge.css"
                >
    
      
<!-- /ew:head_css -->

    
    
      <!-- ew:head_js -->

    
      <script type="text/javascript" src="http://a.fsdn.com/allura/nf/1433526507/_ew_/_slim/js?href=allura%2Fjs%2Fjquery-base.js"></script>
    
      
<!-- /ew:head_js -->

    

    
      <style type="text/css">
        #page-body.project---init-- #top_nav { display: none; }
#page-body.project---init-- #nav_menu_holder { display: none; margin-bottom: 0; }
#page-body.project---init-- #content_base {margin-top: 0; }
      </style>
    
    
    <link rel="alternate" type="application/rss+xml" title="RSS" href="/p/pyserial/code/feed.rss"/>
    <link rel="alternate" type="application/atom+xml" title="Atom" href="/p/pyserial/code/feed.atom"/>

      <style>.XIfHpojZobildBbqCNBIbuEA { display:none }</style>

    
    
    
    


<script type="text/javascript">
    (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
            (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
        m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
    })(window,document,'script','//www.google-analytics.com/analytics.js','ga');

    function _add_tracking(prefix, tracking_id) {
        ga('create', tracking_id, {cookieDomain: 'auto', 'name': prefix});
        
        ga(prefix+'.set', 'dimension9', 'pyserial');
        ga(prefix+'.set', 'dimension10', 'svn');
        ga(prefix+'.send', 'pageview');
    }
      _add_tracking('sfnt1', 'UA-32013-6');
      _add_tracking('sfnt2', 'UA-36130941-1');
    
</script>
  </head>

  <body id="forge">
    <h2 class="hidden">
        <span style="color:red">Error:</span> CSS did not load.<br>
        This may happen on the first request due to CSS mimetype issues.
        Try clearing your browser cache and refreshing.
        <hr>
    </h2>
    
    
      <!-- ew:body_top_js -->

    
      
<!-- /ew:body_top_js -->

    
    
    
<header id="site-header">
    <div class="wrapper">
        <a href="/" class="logo">
            <span>SourceForge</span>
        </a>
        
        <form method="get" action="/directory/">
            <input type="text" id="words" name="q" placeholder="Search">
        </form>
        
        <!--Switch to {language}-->
        <nav id="nav-site">
            <a href="/directory/" title="Browse our software.">Browse</a>
            <a href="/directory/enterprise" title="Browse our Enterprise software.">Enterprise</a>
            <a href="/blog/" title="Read the latest news from the SF HQ.">Blog</a>
            <a href="/jobs?source=header" title="Search 80k+ tech jobs." >Jobs</a>
            <a href="//deals.sourceforge.net/?utm_source=sourceforge&amp;utm_medium=navbar&amp;utm_campaign=homepage" title="Discover and Save on the Best Gear, Gadgets, and Software" class="featured-link" target="_blank">Deals</a>
            <a href="/support" title="Contact us for help and feedback.">Help</a>
        </nav>
        <nav id="nav-account">
            
              <div class="logged_out">
                <a href="/auth/">Log In</a>
                <span>or</span>
                <a href="https://sourceforge.net/user/registration/">Join</a>
              </div>
            
        </nav>
        
    </div>
</header>
<header id="site-sec-header">
    <div class="wrapper">
        <nav id="nav-hubs">
            <h4>Solution Centers</h4>
            <a href="http://goparallel.sourceforge.net/">Go Parallel</a>
            <a href="http://apmsolutions.sourceforge.net/">Performance Central</a>
        </nav>
        <nav id="nav-collateral">
            <a href="http://library.slashdotmedia.com/?source=sfnet_header">Resources</a>
            
            <a href="">Newsletters</a>
            
        </nav>
    </div>
</header>
    
    
    
    
        <div id="site-notification">
            <section class="site-message info" data-notification-id="54f4f2a12670403e2286b4dd">
                <p style="font-size:125%; margin-bottom:5px">Learn how easy it is to sync an existing GitHub or Google Code repo to a SourceForge project! <a class="btn call-to-action" href="http://sourceforge.net/blog/tutorial-how-to-sync-a-github-or-google-code-repo-to-a-sourceforge-project/" style="font-size: 100%; padding: 7px 10px;">See Demo</a></p>
                <a href="" class="btn btn-close">Close</a>
            </section>
        </div>
    
    
    <section id="page-body" class=" neighborhood-Projects project-pyserial mountpoint-code">
	  <div id="nav_menu_holder">
            
            



    
    
    
    
    <nav id="breadcrumbs">
        <ul>
            <li itemscope itemtype="http://data-vocabulary.org/Breadcrumb"><a itemprop="url" href="/">Home</a></li>
            <li itemscope itemtype="http://data-vocabulary.org/Breadcrumb"><a itemprop="url" href="/directory">Browse</a></li>
            
            
                
            
            
            
                <li itemscope itemtype="http://data-vocabulary.org/Breadcrumb"><a itemprop="url" href="/p/">Projects</a></li>
                
            
            
                <li itemscope itemtype="http://data-vocabulary.org/Breadcrumb"><a itemprop="url" href="/p/pyserial/">Python Serial Port Extension</a></li>
                
            
            
                <li itemscope itemtype="http://data-vocabulary.org/Breadcrumb">Code</li>
                
            
        </ul>
    </nav>
    
    
  
    
    
  
  
    
    <h1 class="project_title">
        <a href="/p/pyserial/" class="project_link">Python Serial Port Extension</a>
    </h1>
    
    
    
    <h2 class="project_summary">
        
    </h2>
    
    <div class="brought-by">
        Brought to you by:
        
        
            
                <a href="/u/cliechti/">cliechti</a>
            </div>
    

            
      </div>
      <div id="top_nav" class="">
        
        
<ul class="dropdown">
  
    <li class="">
        <a href="/projects/pyserial/" class="ui-icon-tool-summary-32">
            Summary
        </a>
        
        
    </li>
	
    <li class="">
        <a href="/projects/pyserial/files/" class="ui-icon-tool-files-32">
            Files
        </a>
        
        
    </li>
	
    <li class="">
        <a href="/projects/pyserial/reviews" class="ui-icon-tool-reviews-32">
            Reviews
        </a>
        
        
    </li>
	
    <li class="">
        <a href="/projects/pyserial/support" class="ui-icon-tool-support-32">
            Support
        </a>
        
        
    </li>
	
    <li class="">
        <a href="/p/pyserial/wiki/" class="ui-icon-tool-wiki-32">
            Wiki
        </a>
        
        
    </li>
	
    <li class="">
        <a href="/p/pyserial/_list/tickets" class="ui-icon-tool-tickets-32">
            Tickets ▾
        </a>
        
        
            <ul>
                
                    <li class=""><a href="/p/pyserial/bugs/">Bugs</a></li>
                
                    <li class=""><a href="/p/pyserial/support-requests/">Support Requests</a></li>
                
                    <li class=""><a href="/p/pyserial/patches/">Patches</a></li>
                
                    <li class=""><a href="/p/pyserial/feature-requests/">Feature Requests</a></li>
                
            </ul>
        
    </li>
	
    <li class="">
        <a href="/p/pyserial/news/" class="ui-icon-tool-blog-32">
            News
        </a>
        
        
    </li>
	
    <li class="selected">
        <a href="/p/pyserial/code/" class="ui-icon-tool-svn-32">
            Code
        </a>
        
        
    </li>
	
</ul>

        
      </div>
      <div id="content_base">
      
			  
			    
          


<div id="sidebar">
  
    <div>&nbsp;</div>
  
    
    
      
        
    
      <ul class="sidebarmenu">
      
    
  <li>
      <a href="/p/pyserial/code/commit_browser"   >
       <b data-icon="o" class="ico ico-folder"></b>
      <span>Browse Commits</span>
       </a>
  </li>
  
      
    
    
      </ul>
      
    
    
</div>
          
          
			  
			  
          
        
        <div class="grid-20 pad">
          <h2 class="dark title">
<a href="/p/pyserial/code/508/">[r508]</a>:

  
  
    <a href="./../../">trunk</a> /
    
  
    <a href="./../">pyserial</a> /
    
  
    <a href="./">examples</a> /
    
  
 wxTerminal.py

            <!-- actions -->
            <small>
            

    
    <a id="maximize-content" href="#">
      <b data-icon="`" class="ico ico-expand" title="Maximize"> </b> Maximize
    </a>
    <a id="restore-content" href="#">
      <b data-icon="J" class="ico ico-restore" title="Restore"> </b> Restore
    </a>
<a href="/p/pyserial/code/508/log/?path=/trunk/pyserial/examples/wxTerminal.py">
  <b data-icon="N" class="ico ico-history" title="History"> </b> History
</a>

            </small>
            <!-- /actions -->
          </h2>
		
          <div>
            
  

            
  
    <p><a href="?format=raw">Download this file</a></p>
    <div class="clip grid-19 codebrowser">
      <h3>
        <span class="ico-l"><b data-icon="n" class="ico ico-table"></b> wxTerminal.py</span>
        &nbsp;&nbsp;
        334 lines (290 with data), 13.5 kB
      </h3>
      
        <table class="codehilitetable"><tr><td class="linenos"><div class="linenodiv"><pre>  1
  2
  3
  4
  5
  6
  7
  8
  9
 10
 11
 12
 13
 14
 15
 16
 17
 18
 19
 20
 21
 22
 23
 24
 25
 26
 27
 28
 29
 30
 31
 32
 33
 34
 35
 36
 37
 38
 39
 40
 41
 42
 43
 44
 45
 46
 47
 48
 49
 50
 51
 52
 53
 54
 55
 56
 57
 58
 59
 60
 61
 62
 63
 64
 65
 66
 67
 68
 69
 70
 71
 72
 73
 74
 75
 76
 77
 78
 79
 80
 81
 82
 83
 84
 85
 86
 87
 88
 89
 90
 91
 92
 93
 94
 95
 96
 97
 98
 99
100
101
102
103
104
105
106
107
108
109
110
111
112
113
114
115
116
117
118
119
120
121
122
123
124
125
126
127
128
129
130
131
132
133
134
135
136
137
138
139
140
141
142
143
144
145
146
147
148
149
150
151
152
153
154
155
156
157
158
159
160
161
162
163
164
165
166
167
168
169
170
171
172
173
174
175
176
177
178
179
180
181
182
183
184
185
186
187
188
189
190
191
192
193
194
195
196
197
198
199
200
201
202
203
204
205
206
207
208
209
210
211
212
213
214
215
216
217
218
219
220
221
222
223
224
225
226
227
228
229
230
231
232
233
234
235
236
237
238
239
240
241
242
243
244
245
246
247
248
249
250
251
252
253
254
255
256
257
258
259
260
261
262
263
264
265
266
267
268
269
270
271
272
273
274
275
276
277
278
279
280
281
282
283
284
285
286
287
288
289
290
291
292
293
294
295
296
297
298
299
300
301
302
303
304
305
306
307
308
309
310
311
312
313
314
315
316
317
318
319
320
321
322
323
324
325
326
327
328
329
330
331
332
333</pre></div></td><td class="code"><div class="codehilite"><pre><div id="l1" class="code_block"><span class="c">#!/usr/bin/env python</span>
</div><div id="l2" class="code_block"><span class="c"># generated by wxGlade 0.3.1 on Fri Oct 03 23:23:45 2003</span>
</div><div id="l3" class="code_block">
</div><div id="l4" class="code_block"><span class="c">#from wxPython.wx import *</span>
</div><div id="l5" class="code_block"><span class="kn">import</span> <span class="nn">wx</span>
</div><div id="l6" class="code_block"><span class="kn">import</span> <span class="nn">wxSerialConfigDialog</span>
</div><div id="l7" class="code_block"><span class="kn">import</span> <span class="nn">serial</span>
</div><div id="l8" class="code_block"><span class="kn">import</span> <span class="nn">threading</span>
</div><div id="l9" class="code_block">
</div><div id="l10" class="code_block"><span class="c">#----------------------------------------------------------------------</span>
</div><div id="l11" class="code_block"><span class="c"># Create an own event type, so that GUI updates can be delegated</span>
</div><div id="l12" class="code_block"><span class="c"># this is required as on some platforms only the main thread can</span>
</div><div id="l13" class="code_block"><span class="c"># access the GUI without crashing. wxMutexGuiEnter/wxMutexGuiLeave</span>
</div><div id="l14" class="code_block"><span class="c"># could be used too, but an event is more elegant.</span>
</div><div id="l15" class="code_block">
</div><div id="l16" class="code_block"><span class="n">SERIALRX</span> <span class="o">=</span> <span class="n">wx</span><span class="o">.</span><span class="n">NewEventType</span><span class="p">()</span>
</div><div id="l17" class="code_block"><span class="c"># bind to serial data receive events</span>
</div><div id="l18" class="code_block"><span class="n">EVT_SERIALRX</span> <span class="o">=</span> <span class="n">wx</span><span class="o">.</span><span class="n">PyEventBinder</span><span class="p">(</span><span class="n">SERIALRX</span><span class="p">,</span> <span class="mi">0</span><span class="p">)</span>
</div><div id="l19" class="code_block">
</div><div id="l20" class="code_block"><span class="k">class</span> <span class="nc">SerialRxEvent</span><span class="p">(</span><span class="n">wx</span><span class="o">.</span><span class="n">PyCommandEvent</span><span class="p">):</span>
</div><div id="l21" class="code_block">    <span class="n">eventType</span> <span class="o">=</span> <span class="n">SERIALRX</span>
</div><div id="l22" class="code_block">    <span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">windowID</span><span class="p">,</span> <span class="n">data</span><span class="p">):</span>
</div><div id="l23" class="code_block">        <span class="n">wx</span><span class="o">.</span><span class="n">PyCommandEvent</span><span class="o">.</span><span class="n">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">eventType</span><span class="p">,</span> <span class="n">windowID</span><span class="p">)</span>
</div><div id="l24" class="code_block">        <span class="bp">self</span><span class="o">.</span><span class="n">data</span> <span class="o">=</span> <span class="n">data</span>
</div><div id="l25" class="code_block">
</div><div id="l26" class="code_block">    <span class="k">def</span> <span class="nf">Clone</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</div><div id="l27" class="code_block">        <span class="bp">self</span><span class="o">.</span><span class="n">__class__</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">GetId</span><span class="p">(),</span> <span class="bp">self</span><span class="o">.</span><span class="n">data</span><span class="p">)</span>
</div><div id="l28" class="code_block">
</div><div id="l29" class="code_block"><span class="c">#----------------------------------------------------------------------</span>
</div><div id="l30" class="code_block">
</div><div id="l31" class="code_block"><span class="n">ID_CLEAR</span>        <span class="o">=</span> <span class="n">wx</span><span class="o">.</span><span class="n">NewId</span><span class="p">()</span>
</div><div id="l32" class="code_block"><span class="n">ID_SAVEAS</span>       <span class="o">=</span> <span class="n">wx</span><span class="o">.</span><span class="n">NewId</span><span class="p">()</span>
</div><div id="l33" class="code_block"><span class="n">ID_SETTINGS</span>     <span class="o">=</span> <span class="n">wx</span><span class="o">.</span><span class="n">NewId</span><span class="p">()</span>
</div><div id="l34" class="code_block"><span class="n">ID_TERM</span>         <span class="o">=</span> <span class="n">wx</span><span class="o">.</span><span class="n">NewId</span><span class="p">()</span>
</div><div id="l35" class="code_block"><span class="n">ID_EXIT</span>         <span class="o">=</span> <span class="n">wx</span><span class="o">.</span><span class="n">NewId</span><span class="p">()</span>
</div><div id="l36" class="code_block">
</div><div id="l37" class="code_block"><span class="n">NEWLINE_CR</span>      <span class="o">=</span> <span class="mi">0</span>
</div><div id="l38" class="code_block"><span class="n">NEWLINE_LF</span>      <span class="o">=</span> <span class="mi">1</span>
</div><div id="l39" class="code_block"><span class="n">NEWLINE_CRLF</span>    <span class="o">=</span> <span class="mi">2</span>
</div><div id="l40" class="code_block">
</div><div id="l41" class="code_block"><span class="k">class</span> <span class="nc">TerminalSetup</span><span class="p">:</span>
</div><div id="l42" class="code_block">    <span class="sd">&quot;&quot;&quot;Placeholder for various terminal settings. Used to pass the</span>
</div><div id="l43" class="code_block"><span class="sd">       options to the TerminalSettingsDialog.&quot;&quot;&quot;</span>
</div><div id="l44" class="code_block">    <span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</div><div id="l45" class="code_block">        <span class="bp">self</span><span class="o">.</span><span class="n">echo</span> <span class="o">=</span> <span class="bp">False</span>
</div><div id="l46" class="code_block">        <span class="bp">self</span><span class="o">.</span><span class="n">unprintable</span> <span class="o">=</span> <span class="bp">False</span>
</div><div id="l47" class="code_block">        <span class="bp">self</span><span class="o">.</span><span class="n">newline</span> <span class="o">=</span> <span class="n">NEWLINE_CRLF</span>
</div><div id="l48" class="code_block">
</div><div id="l49" class="code_block"><span class="k">class</span> <span class="nc">TerminalSettingsDialog</span><span class="p">(</span><span class="n">wx</span><span class="o">.</span><span class="n">Dialog</span><span class="p">):</span>
</div><div id="l50" class="code_block">    <span class="sd">&quot;&quot;&quot;Simple dialog with common terminal settings like echo, newline mode.&quot;&quot;&quot;</span>
</div><div id="l51" class="code_block">    
</div><div id="l52" class="code_block">    <span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwds</span><span class="p">):</span>
</div><div id="l53" class="code_block">        <span class="bp">self</span><span class="o">.</span><span class="n">settings</span> <span class="o">=</span> <span class="n">kwds</span><span class="p">[</span><span class="s">&#39;settings&#39;</span><span class="p">]</span>
</div><div id="l54" class="code_block">        <span class="k">del</span> <span class="n">kwds</span><span class="p">[</span><span class="s">&#39;settings&#39;</span><span class="p">]</span>
</div><div id="l55" class="code_block">        <span class="c"># begin wxGlade: TerminalSettingsDialog.__init__</span>
</div><div id="l56" class="code_block">        <span class="n">kwds</span><span class="p">[</span><span class="s">&quot;style&quot;</span><span class="p">]</span> <span class="o">=</span> <span class="n">wx</span><span class="o">.</span><span class="n">DEFAULT_DIALOG_STYLE</span>
</div><div id="l57" class="code_block">        <span class="n">wx</span><span class="o">.</span><span class="n">Dialog</span><span class="o">.</span><span class="n">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwds</span><span class="p">)</span>
</div><div id="l58" class="code_block">        <span class="bp">self</span><span class="o">.</span><span class="n">checkbox_echo</span> <span class="o">=</span> <span class="n">wx</span><span class="o">.</span><span class="n">CheckBox</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">-</span><span class="mi">1</span><span class="p">,</span> <span class="s">&quot;Local Echo&quot;</span><span class="p">)</span>
</div><div id="l59" class="code_block">        <span class="bp">self</span><span class="o">.</span><span class="n">checkbox_unprintable</span> <span class="o">=</span> <span class="n">wx</span><span class="o">.</span><span class="n">CheckBox</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">-</span><span class="mi">1</span><span class="p">,</span> <span class="s">&quot;Show unprintable characters&quot;</span><span class="p">)</span>
</div><div id="l60" class="code_block">        <span class="bp">self</span><span class="o">.</span><span class="n">radio_box_newline</span> <span class="o">=</span> <span class="n">wx</span><span class="o">.</span><span class="n">RadioBox</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">-</span><span class="mi">1</span><span class="p">,</span> <span class="s">&quot;Newline Handling&quot;</span><span class="p">,</span> <span class="n">choices</span><span class="o">=</span><span class="p">[</span><span class="s">&quot;CR only&quot;</span><span class="p">,</span> <span class="s">&quot;LF only&quot;</span><span class="p">,</span> <span class="s">&quot;CR+LF&quot;</span><span class="p">],</span> <span class="n">majorDimension</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span> <span class="n">style</span><span class="o">=</span><span class="n">wx</span><span class="o">.</span><span class="n">RA_SPECIFY_ROWS</span><span class="p">)</span>
</div><div id="l61" class="code_block">        <span class="bp">self</span><span class="o">.</span><span class="n">button_ok</span> <span class="o">=</span> <span class="n">wx</span><span class="o">.</span><span class="n">Button</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">-</span><span class="mi">1</span><span class="p">,</span> <span class="s">&quot;OK&quot;</span><span class="p">)</span>
</div><div id="l62" class="code_block">        <span class="bp">self</span><span class="o">.</span><span class="n">button_cancel</span> <span class="o">=</span> <span class="n">wx</span><span class="o">.</span><span class="n">Button</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">-</span><span class="mi">1</span><span class="p">,</span> <span class="s">&quot;Cancel&quot;</span><span class="p">)</span>
</div><div id="l63" class="code_block">
</div><div id="l64" class="code_block">        <span class="bp">self</span><span class="o">.</span><span class="n">__set_properties</span><span class="p">()</span>
</div><div id="l65" class="code_block">        <span class="bp">self</span><span class="o">.</span><span class="n">__do_layout</span><span class="p">()</span>
</div><div id="l66" class="code_block">        <span class="c"># end wxGlade</span>
</div><div id="l67" class="code_block">        <span class="bp">self</span><span class="o">.</span><span class="n">__attach_events</span><span class="p">()</span>
</div><div id="l68" class="code_block">        <span class="bp">self</span><span class="o">.</span><span class="n">checkbox_echo</span><span class="o">.</span><span class="n">SetValue</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">echo</span><span class="p">)</span>
</div><div id="l69" class="code_block">        <span class="bp">self</span><span class="o">.</span><span class="n">checkbox_unprintable</span><span class="o">.</span><span class="n">SetValue</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">unprintable</span><span class="p">)</span>
</div><div id="l70" class="code_block">        <span class="bp">self</span><span class="o">.</span><span class="n">radio_box_newline</span><span class="o">.</span><span class="n">SetSelection</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">newline</span><span class="p">)</span>
</div><div id="l71" class="code_block">
</div><div id="l72" class="code_block">    <span class="k">def</span> <span class="nf">__set_properties</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</div><div id="l73" class="code_block">        <span class="c"># begin wxGlade: TerminalSettingsDialog.__set_properties</span>
</div><div id="l74" class="code_block">        <span class="bp">self</span><span class="o">.</span><span class="n">SetTitle</span><span class="p">(</span><span class="s">&quot;Terminal Settings&quot;</span><span class="p">)</span>
</div><div id="l75" class="code_block">        <span class="bp">self</span><span class="o">.</span><span class="n">radio_box_newline</span><span class="o">.</span><span class="n">SetSelection</span><span class="p">(</span><span class="mi">0</span><span class="p">)</span>
</div><div id="l76" class="code_block">        <span class="bp">self</span><span class="o">.</span><span class="n">button_ok</span><span class="o">.</span><span class="n">SetDefault</span><span class="p">()</span>
</div><div id="l77" class="code_block">        <span class="c"># end wxGlade</span>
</div><div id="l78" class="code_block">
</div><div id="l79" class="code_block">    <span class="k">def</span> <span class="nf">__do_layout</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</div><div id="l80" class="code_block">        <span class="c"># begin wxGlade: TerminalSettingsDialog.__do_layout</span>
</div><div id="l81" class="code_block">        <span class="n">sizer_2</span> <span class="o">=</span> <span class="n">wx</span><span class="o">.</span><span class="n">BoxSizer</span><span class="p">(</span><span class="n">wx</span><span class="o">.</span><span class="n">VERTICAL</span><span class="p">)</span>
</div><div id="l82" class="code_block">        <span class="n">sizer_3</span> <span class="o">=</span> <span class="n">wx</span><span class="o">.</span><span class="n">BoxSizer</span><span class="p">(</span><span class="n">wx</span><span class="o">.</span><span class="n">HORIZONTAL</span><span class="p">)</span>
</div><div id="l83" class="code_block">        <span class="n">sizer_4</span> <span class="o">=</span> <span class="n">wx</span><span class="o">.</span><span class="n">StaticBoxSizer</span><span class="p">(</span><span class="n">wx</span><span class="o">.</span><span class="n">StaticBox</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">-</span><span class="mi">1</span><span class="p">,</span> <span class="s">&quot;Input/Output&quot;</span><span class="p">),</span> <span class="n">wx</span><span class="o">.</span><span class="n">VERTICAL</span><span class="p">)</span>
</div><div id="l84" class="code_block">        <span class="n">sizer_4</span><span class="o">.</span><span class="n">Add</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">checkbox_echo</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="n">wx</span><span class="o">.</span><span class="n">ALL</span><span class="p">,</span> <span class="mi">4</span><span class="p">)</span>
</div><div id="l85" class="code_block">        <span class="n">sizer_4</span><span class="o">.</span><span class="n">Add</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">checkbox_unprintable</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="n">wx</span><span class="o">.</span><span class="n">ALL</span><span class="p">,</span> <span class="mi">4</span><span class="p">)</span>
</div><div id="l86" class="code_block">        <span class="n">sizer_4</span><span class="o">.</span><span class="n">Add</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">radio_box_newline</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">0</span><span class="p">)</span>
</div><div id="l87" class="code_block">        <span class="n">sizer_2</span><span class="o">.</span><span class="n">Add</span><span class="p">(</span><span class="n">sizer_4</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="n">wx</span><span class="o">.</span><span class="n">EXPAND</span><span class="p">,</span> <span class="mi">0</span><span class="p">)</span>
</div><div id="l88" class="code_block">        <span class="n">sizer_3</span><span class="o">.</span><span class="n">Add</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">button_ok</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">0</span><span class="p">)</span>
</div><div id="l89" class="code_block">        <span class="n">sizer_3</span><span class="o">.</span><span class="n">Add</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">button_cancel</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">0</span><span class="p">)</span>
</div><div id="l90" class="code_block">        <span class="n">sizer_2</span><span class="o">.</span><span class="n">Add</span><span class="p">(</span><span class="n">sizer_3</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="n">wx</span><span class="o">.</span><span class="n">ALL</span><span class="o">|</span><span class="n">wx</span><span class="o">.</span><span class="n">ALIGN_RIGHT</span><span class="p">,</span> <span class="mi">4</span><span class="p">)</span>
</div><div id="l91" class="code_block">        <span class="bp">self</span><span class="o">.</span><span class="n">SetAutoLayout</span><span class="p">(</span><span class="mi">1</span><span class="p">)</span>
</div><div id="l92" class="code_block">        <span class="bp">self</span><span class="o">.</span><span class="n">SetSizer</span><span class="p">(</span><span class="n">sizer_2</span><span class="p">)</span>
</div><div id="l93" class="code_block">        <span class="n">sizer_2</span><span class="o">.</span><span class="n">Fit</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span>
</div><div id="l94" class="code_block">        <span class="n">sizer_2</span><span class="o">.</span><span class="n">SetSizeHints</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span>
</div><div id="l95" class="code_block">        <span class="bp">self</span><span class="o">.</span><span class="n">Layout</span><span class="p">()</span>
</div><div id="l96" class="code_block">        <span class="c"># end wxGlade</span>
</div><div id="l97" class="code_block">
</div><div id="l98" class="code_block">    <span class="k">def</span> <span class="nf">__attach_events</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</div><div id="l99" class="code_block">        <span class="bp">self</span><span class="o">.</span><span class="n">Bind</span><span class="p">(</span><span class="n">wx</span><span class="o">.</span><span class="n">EVT_BUTTON</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">OnOK</span><span class="p">,</span> <span class="nb">id</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">button_ok</span><span class="o">.</span><span class="n">GetId</span><span class="p">())</span>
</div><div id="l100" class="code_block">        <span class="bp">self</span><span class="o">.</span><span class="n">Bind</span><span class="p">(</span><span class="n">wx</span><span class="o">.</span><span class="n">EVT_BUTTON</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">OnCancel</span><span class="p">,</span> <span class="nb">id</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">button_cancel</span><span class="o">.</span><span class="n">GetId</span><span class="p">())</span>
</div><div id="l101" class="code_block">    
</div><div id="l102" class="code_block">    <span class="k">def</span> <span class="nf">OnOK</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">events</span><span class="p">):</span>
</div><div id="l103" class="code_block">        <span class="sd">&quot;&quot;&quot;Update data wil new values and close dialog.&quot;&quot;&quot;</span>
</div><div id="l104" class="code_block">        <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">echo</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">checkbox_echo</span><span class="o">.</span><span class="n">GetValue</span><span class="p">()</span>
</div><div id="l105" class="code_block">        <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">unprintable</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">checkbox_unprintable</span><span class="o">.</span><span class="n">GetValue</span><span class="p">()</span>
</div><div id="l106" class="code_block">        <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">newline</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">radio_box_newline</span><span class="o">.</span><span class="n">GetSelection</span><span class="p">()</span>
</div><div id="l107" class="code_block">        <span class="bp">self</span><span class="o">.</span><span class="n">EndModal</span><span class="p">(</span><span class="n">wx</span><span class="o">.</span><span class="n">ID_OK</span><span class="p">)</span>
</div><div id="l108" class="code_block">    
</div><div id="l109" class="code_block">    <span class="k">def</span> <span class="nf">OnCancel</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">events</span><span class="p">):</span>
</div><div id="l110" class="code_block">        <span class="sd">&quot;&quot;&quot;Do not update data but close dialog.&quot;&quot;&quot;</span>
</div><div id="l111" class="code_block">        <span class="bp">self</span><span class="o">.</span><span class="n">EndModal</span><span class="p">(</span><span class="n">wx</span><span class="o">.</span><span class="n">ID_CANCEL</span><span class="p">)</span>
</div><div id="l112" class="code_block">
</div><div id="l113" class="code_block"><span class="c"># end of class TerminalSettingsDialog</span>
</div><div id="l114" class="code_block">
</div><div id="l115" class="code_block">
</div><div id="l116" class="code_block"><span class="k">class</span> <span class="nc">TerminalFrame</span><span class="p">(</span><span class="n">wx</span><span class="o">.</span><span class="n">Frame</span><span class="p">):</span>
</div><div id="l117" class="code_block">    <span class="sd">&quot;&quot;&quot;Simple terminal program for wxPython&quot;&quot;&quot;</span>
</div><div id="l118" class="code_block">    
</div><div id="l119" class="code_block">    <span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwds</span><span class="p">):</span>
</div><div id="l120" class="code_block">        <span class="bp">self</span><span class="o">.</span><span class="n">serial</span> <span class="o">=</span> <span class="n">serial</span><span class="o">.</span><span class="n">Serial</span><span class="p">()</span>
</div><div id="l121" class="code_block">        <span class="bp">self</span><span class="o">.</span><span class="n">serial</span><span class="o">.</span><span class="n">timeout</span> <span class="o">=</span> <span class="mf">0.5</span>   <span class="c">#make sure that the alive event can be checked from time to time</span>
</div><div id="l122" class="code_block">        <span class="bp">self</span><span class="o">.</span><span class="n">settings</span> <span class="o">=</span> <span class="n">TerminalSetup</span><span class="p">()</span> <span class="c">#placeholder for the settings</span>
</div><div id="l123" class="code_block">        <span class="bp">self</span><span class="o">.</span><span class="n">thread</span> <span class="o">=</span> <span class="bp">None</span>
</div><div id="l124" class="code_block">        <span class="bp">self</span><span class="o">.</span><span class="n">alive</span> <span class="o">=</span> <span class="n">threading</span><span class="o">.</span><span class="n">Event</span><span class="p">()</span>               
</div><div id="l125" class="code_block">        <span class="c"># begin wxGlade: TerminalFrame.__init__</span>
</div><div id="l126" class="code_block">        <span class="n">kwds</span><span class="p">[</span><span class="s">&quot;style&quot;</span><span class="p">]</span> <span class="o">=</span> <span class="n">wx</span><span class="o">.</span><span class="n">DEFAULT_FRAME_STYLE</span>
</div><div id="l127" class="code_block">        <span class="n">wx</span><span class="o">.</span><span class="n">Frame</span><span class="o">.</span><span class="n">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwds</span><span class="p">)</span>
</div><div id="l128" class="code_block">        <span class="bp">self</span><span class="o">.</span><span class="n">text_ctrl_output</span> <span class="o">=</span> <span class="n">wx</span><span class="o">.</span><span class="n">TextCtrl</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">-</span><span class="mi">1</span><span class="p">,</span> <span class="s">&quot;&quot;</span><span class="p">,</span> <span class="n">style</span><span class="o">=</span><span class="n">wx</span><span class="o">.</span><span class="n">TE_MULTILINE</span><span class="o">|</span><span class="n">wx</span><span class="o">.</span><span class="n">TE_READONLY</span><span class="p">)</span>
</div><div id="l129" class="code_block">        
</div><div id="l130" class="code_block">        <span class="c"># Menu Bar</span>
</div><div id="l131" class="code_block">        <span class="bp">self</span><span class="o">.</span><span class="n">frame_terminal_menubar</span> <span class="o">=</span> <span class="n">wx</span><span class="o">.</span><span class="n">MenuBar</span><span class="p">()</span>
</div><div id="l132" class="code_block">        <span class="bp">self</span><span class="o">.</span><span class="n">SetMenuBar</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">frame_terminal_menubar</span><span class="p">)</span>
</div><div id="l133" class="code_block">        <span class="n">wxglade_tmp_menu</span> <span class="o">=</span> <span class="n">wx</span><span class="o">.</span><span class="n">Menu</span><span class="p">()</span>
</div><div id="l134" class="code_block">        <span class="n">wxglade_tmp_menu</span><span class="o">.</span><span class="n">Append</span><span class="p">(</span><span class="n">ID_CLEAR</span><span class="p">,</span> <span class="s">&quot;&amp;Clear&quot;</span><span class="p">,</span> <span class="s">&quot;&quot;</span><span class="p">,</span> <span class="n">wx</span><span class="o">.</span><span class="n">ITEM_NORMAL</span><span class="p">)</span>
</div><div id="l135" class="code_block">        <span class="n">wxglade_tmp_menu</span><span class="o">.</span><span class="n">Append</span><span class="p">(</span><span class="n">ID_SAVEAS</span><span class="p">,</span> <span class="s">&quot;&amp;Save Text As...&quot;</span><span class="p">,</span> <span class="s">&quot;&quot;</span><span class="p">,</span> <span class="n">wx</span><span class="o">.</span><span class="n">ITEM_NORMAL</span><span class="p">)</span>
</div><div id="l136" class="code_block">        <span class="n">wxglade_tmp_menu</span><span class="o">.</span><span class="n">AppendSeparator</span><span class="p">()</span>
</div><div id="l137" class="code_block">        <span class="n">wxglade_tmp_menu</span><span class="o">.</span><span class="n">Append</span><span class="p">(</span><span class="n">ID_SETTINGS</span><span class="p">,</span> <span class="s">&quot;&amp;Port Settings...&quot;</span><span class="p">,</span> <span class="s">&quot;&quot;</span><span class="p">,</span> <span class="n">wx</span><span class="o">.</span><span class="n">ITEM_NORMAL</span><span class="p">)</span>
</div><div id="l138" class="code_block">        <span class="n">wxglade_tmp_menu</span><span class="o">.</span><span class="n">Append</span><span class="p">(</span><span class="n">ID_TERM</span><span class="p">,</span> <span class="s">&quot;&amp;Terminal Settings...&quot;</span><span class="p">,</span> <span class="s">&quot;&quot;</span><span class="p">,</span> <span class="n">wx</span><span class="o">.</span><span class="n">ITEM_NORMAL</span><span class="p">)</span>
</div><div id="l139" class="code_block">        <span class="n">wxglade_tmp_menu</span><span class="o">.</span><span class="n">AppendSeparator</span><span class="p">()</span>
</div><div id="l140" class="code_block">        <span class="n">wxglade_tmp_menu</span><span class="o">.</span><span class="n">Append</span><span class="p">(</span><span class="n">ID_EXIT</span><span class="p">,</span> <span class="s">&quot;&amp;Exit&quot;</span><span class="p">,</span> <span class="s">&quot;&quot;</span><span class="p">,</span> <span class="n">wx</span><span class="o">.</span><span class="n">ITEM_NORMAL</span><span class="p">)</span>
</div><div id="l141" class="code_block">        <span class="bp">self</span><span class="o">.</span><span class="n">frame_terminal_menubar</span><span class="o">.</span><span class="n">Append</span><span class="p">(</span><span class="n">wxglade_tmp_menu</span><span class="p">,</span> <span class="s">&quot;&amp;File&quot;</span><span class="p">)</span>
</div><div id="l142" class="code_block">        <span class="c"># Menu Bar end</span>
</div><div id="l143" class="code_block">
</div><div id="l144" class="code_block">        <span class="bp">self</span><span class="o">.</span><span class="n">__set_properties</span><span class="p">()</span>
</div><div id="l145" class="code_block">        <span class="bp">self</span><span class="o">.</span><span class="n">__do_layout</span><span class="p">()</span>
</div><div id="l146" class="code_block">        <span class="c"># end wxGlade</span>
</div><div id="l147" class="code_block">        <span class="bp">self</span><span class="o">.</span><span class="n">__attach_events</span><span class="p">()</span>          <span class="c">#register events</span>
</div><div id="l148" class="code_block">        <span class="bp">self</span><span class="o">.</span><span class="n">OnPortSettings</span><span class="p">(</span><span class="bp">None</span><span class="p">)</span>       <span class="c">#call setup dialog on startup, opens port</span>
</div><div id="l149" class="code_block">        <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">alive</span><span class="o">.</span><span class="n">isSet</span><span class="p">():</span>
</div><div id="l150" class="code_block">            <span class="bp">self</span><span class="o">.</span><span class="n">Close</span><span class="p">()</span>
</div><div id="l151" class="code_block">
</div><div id="l152" class="code_block">    <span class="k">def</span> <span class="nf">StartThread</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</div><div id="l153" class="code_block">        <span class="sd">&quot;&quot;&quot;Start the receiver thread&quot;&quot;&quot;</span>        
</div><div id="l154" class="code_block">        <span class="bp">self</span><span class="o">.</span><span class="n">thread</span> <span class="o">=</span> <span class="n">threading</span><span class="o">.</span><span class="n">Thread</span><span class="p">(</span><span class="n">target</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">ComPortThread</span><span class="p">)</span>
</div><div id="l155" class="code_block">        <span class="bp">self</span><span class="o">.</span><span class="n">thread</span><span class="o">.</span><span class="n">setDaemon</span><span class="p">(</span><span class="mi">1</span><span class="p">)</span>
</div><div id="l156" class="code_block">        <span class="bp">self</span><span class="o">.</span><span class="n">alive</span><span class="o">.</span><span class="n">set</span><span class="p">()</span>
</div><div id="l157" class="code_block">        <span class="bp">self</span><span class="o">.</span><span class="n">thread</span><span class="o">.</span><span class="n">start</span><span class="p">()</span>
</div><div id="l158" class="code_block">
</div><div id="l159" class="code_block">    <span class="k">def</span> <span class="nf">StopThread</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</div><div id="l160" class="code_block">        <span class="sd">&quot;&quot;&quot;Stop the receiver thread, wait util it&#39;s finished.&quot;&quot;&quot;</span>
</div><div id="l161" class="code_block">        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">thread</span> <span class="ow">is</span> <span class="ow">not</span> <span class="bp">None</span><span class="p">:</span>
</div><div id="l162" class="code_block">            <span class="bp">self</span><span class="o">.</span><span class="n">alive</span><span class="o">.</span><span class="n">clear</span><span class="p">()</span>          <span class="c">#clear alive event for thread</span>
</div><div id="l163" class="code_block">            <span class="bp">self</span><span class="o">.</span><span class="n">thread</span><span class="o">.</span><span class="n">join</span><span class="p">()</span>          <span class="c">#wait until thread has finished</span>
</div><div id="l164" class="code_block">            <span class="bp">self</span><span class="o">.</span><span class="n">thread</span> <span class="o">=</span> <span class="bp">None</span>
</div><div id="l165" class="code_block">        
</div><div id="l166" class="code_block">    <span class="k">def</span> <span class="nf">__set_properties</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</div><div id="l167" class="code_block">        <span class="c"># begin wxGlade: TerminalFrame.__set_properties</span>
</div><div id="l168" class="code_block">        <span class="bp">self</span><span class="o">.</span><span class="n">SetTitle</span><span class="p">(</span><span class="s">&quot;Serial Terminal&quot;</span><span class="p">)</span>
</div><div id="l169" class="code_block">        <span class="bp">self</span><span class="o">.</span><span class="n">SetSize</span><span class="p">((</span><span class="mi">546</span><span class="p">,</span> <span class="mi">383</span><span class="p">))</span>
</div><div id="l170" class="code_block">        <span class="c"># end wxGlade</span>
</div><div id="l171" class="code_block">
</div><div id="l172" class="code_block">    <span class="k">def</span> <span class="nf">__do_layout</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</div><div id="l173" class="code_block">        <span class="c"># begin wxGlade: TerminalFrame.__do_layout</span>
</div><div id="l174" class="code_block">        <span class="n">sizer_1</span> <span class="o">=</span> <span class="n">wx</span><span class="o">.</span><span class="n">BoxSizer</span><span class="p">(</span><span class="n">wx</span><span class="o">.</span><span class="n">VERTICAL</span><span class="p">)</span>
</div><div id="l175" class="code_block">        <span class="n">sizer_1</span><span class="o">.</span><span class="n">Add</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">text_ctrl_output</span><span class="p">,</span> <span class="mi">1</span><span class="p">,</span> <span class="n">wx</span><span class="o">.</span><span class="n">EXPAND</span><span class="p">,</span> <span class="mi">0</span><span class="p">)</span>
</div><div id="l176" class="code_block">        <span class="bp">self</span><span class="o">.</span><span class="n">SetAutoLayout</span><span class="p">(</span><span class="mi">1</span><span class="p">)</span>
</div><div id="l177" class="code_block">        <span class="bp">self</span><span class="o">.</span><span class="n">SetSizer</span><span class="p">(</span><span class="n">sizer_1</span><span class="p">)</span>
</div><div id="l178" class="code_block">        <span class="bp">self</span><span class="o">.</span><span class="n">Layout</span><span class="p">()</span>
</div><div id="l179" class="code_block">        <span class="c"># end wxGlade</span>
</div><div id="l180" class="code_block">
</div><div id="l181" class="code_block">    <span class="k">def</span> <span class="nf">__attach_events</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</div><div id="l182" class="code_block">        <span class="c">#register events at the controls</span>
</div><div id="l183" class="code_block">        <span class="bp">self</span><span class="o">.</span><span class="n">Bind</span><span class="p">(</span><span class="n">wx</span><span class="o">.</span><span class="n">EVT_MENU</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">OnClear</span><span class="p">,</span> <span class="nb">id</span> <span class="o">=</span> <span class="n">ID_CLEAR</span><span class="p">)</span>
</div><div id="l184" class="code_block">        <span class="bp">self</span><span class="o">.</span><span class="n">Bind</span><span class="p">(</span><span class="n">wx</span><span class="o">.</span><span class="n">EVT_MENU</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">OnSaveAs</span><span class="p">,</span> <span class="nb">id</span> <span class="o">=</span> <span class="n">ID_SAVEAS</span><span class="p">)</span>
</div><div id="l185" class="code_block">        <span class="bp">self</span><span class="o">.</span><span class="n">Bind</span><span class="p">(</span><span class="n">wx</span><span class="o">.</span><span class="n">EVT_MENU</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">OnExit</span><span class="p">,</span> <span class="nb">id</span> <span class="o">=</span> <span class="n">ID_EXIT</span><span class="p">)</span>
</div><div id="l186" class="code_block">        <span class="bp">self</span><span class="o">.</span><span class="n">Bind</span><span class="p">(</span><span class="n">wx</span><span class="o">.</span><span class="n">EVT_MENU</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">OnPortSettings</span><span class="p">,</span> <span class="nb">id</span> <span class="o">=</span> <span class="n">ID_SETTINGS</span><span class="p">)</span>
</div><div id="l187" class="code_block">        <span class="bp">self</span><span class="o">.</span><span class="n">Bind</span><span class="p">(</span><span class="n">wx</span><span class="o">.</span><span class="n">EVT_MENU</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">OnTermSettings</span><span class="p">,</span> <span class="nb">id</span> <span class="o">=</span> <span class="n">ID_TERM</span><span class="p">)</span>
</div><div id="l188" class="code_block">        <span class="bp">self</span><span class="o">.</span><span class="n">text_ctrl_output</span><span class="o">.</span><span class="n">Bind</span><span class="p">(</span><span class="n">wx</span><span class="o">.</span><span class="n">EVT_CHAR</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">OnKey</span><span class="p">)</span>        
</div><div id="l189" class="code_block">        <span class="bp">self</span><span class="o">.</span><span class="n">Bind</span><span class="p">(</span><span class="n">EVT_SERIALRX</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">OnSerialRead</span><span class="p">)</span>
</div><div id="l190" class="code_block">        <span class="bp">self</span><span class="o">.</span><span class="n">Bind</span><span class="p">(</span><span class="n">wx</span><span class="o">.</span><span class="n">EVT_CLOSE</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">OnClose</span><span class="p">)</span>
</div><div id="l191" class="code_block">
</div><div id="l192" class="code_block">    <span class="k">def</span> <span class="nf">OnExit</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">event</span><span class="p">):</span>
</div><div id="l193" class="code_block">        <span class="sd">&quot;&quot;&quot;Menu point Exit&quot;&quot;&quot;</span>
</div><div id="l194" class="code_block">        <span class="bp">self</span><span class="o">.</span><span class="n">Close</span><span class="p">()</span>
</div><div id="l195" class="code_block">
</div><div id="l196" class="code_block">    <span class="k">def</span> <span class="nf">OnClose</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">event</span><span class="p">):</span>
</div><div id="l197" class="code_block">        <span class="sd">&quot;&quot;&quot;Called on application shutdown.&quot;&quot;&quot;</span>
</div><div id="l198" class="code_block">        <span class="bp">self</span><span class="o">.</span><span class="n">StopThread</span><span class="p">()</span>               <span class="c">#stop reader thread</span>
</div><div id="l199" class="code_block">        <span class="bp">self</span><span class="o">.</span><span class="n">serial</span><span class="o">.</span><span class="n">close</span><span class="p">()</span>             <span class="c">#cleanup</span>
</div><div id="l200" class="code_block">        <span class="bp">self</span><span class="o">.</span><span class="n">Destroy</span><span class="p">()</span>                  <span class="c">#close windows, exit app</span>
</div><div id="l201" class="code_block">
</div><div id="l202" class="code_block">    <span class="k">def</span> <span class="nf">OnSaveAs</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">event</span><span class="p">):</span>
</div><div id="l203" class="code_block">        <span class="sd">&quot;&quot;&quot;Save contents of output window.&quot;&quot;&quot;</span>
</div><div id="l204" class="code_block">        <span class="n">filename</span> <span class="o">=</span> <span class="bp">None</span>
</div><div id="l205" class="code_block">        <span class="n">dlg</span> <span class="o">=</span> <span class="n">wx</span><span class="o">.</span><span class="n">FileDialog</span><span class="p">(</span><span class="bp">None</span><span class="p">,</span> <span class="s">&quot;Save Text As...&quot;</span><span class="p">,</span> <span class="s">&quot;.&quot;</span><span class="p">,</span> <span class="s">&quot;&quot;</span><span class="p">,</span> <span class="s">&quot;Text File|*.txt|All Files|*&quot;</span><span class="p">,</span>  <span class="n">wx</span><span class="o">.</span><span class="n">SAVE</span><span class="p">)</span>
</div><div id="l206" class="code_block">        <span class="k">if</span> <span class="n">dlg</span><span class="o">.</span><span class="n">ShowModal</span><span class="p">()</span> <span class="o">==</span>  <span class="n">wx</span><span class="o">.</span><span class="n">ID_OK</span><span class="p">:</span>
</div><div id="l207" class="code_block">            <span class="n">filename</span> <span class="o">=</span> <span class="n">dlg</span><span class="o">.</span><span class="n">GetPath</span><span class="p">()</span>
</div><div id="l208" class="code_block">        <span class="n">dlg</span><span class="o">.</span><span class="n">Destroy</span><span class="p">()</span>
</div><div id="l209" class="code_block">        
</div><div id="l210" class="code_block">        <span class="k">if</span> <span class="n">filename</span> <span class="ow">is</span> <span class="ow">not</span> <span class="bp">None</span><span class="p">:</span>
</div><div id="l211" class="code_block">            <span class="n">f</span> <span class="o">=</span> <span class="nb">file</span><span class="p">(</span><span class="n">filename</span><span class="p">,</span> <span class="s">&#39;w&#39;</span><span class="p">)</span>
</div><div id="l212" class="code_block">            <span class="n">text</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">text_ctrl_output</span><span class="o">.</span><span class="n">GetValue</span><span class="p">()</span>
</div><div id="l213" class="code_block">            <span class="k">if</span> <span class="nb">type</span><span class="p">(</span><span class="n">text</span><span class="p">)</span> <span class="o">==</span> <span class="nb">unicode</span><span class="p">:</span>
</div><div id="l214" class="code_block">                <span class="n">text</span> <span class="o">=</span> <span class="n">text</span><span class="o">.</span><span class="n">encode</span><span class="p">(</span><span class="s">&quot;latin1&quot;</span><span class="p">)</span>    <span class="c">#hm, is that a good asumption?</span>
</div><div id="l215" class="code_block">            <span class="n">f</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="n">text</span><span class="p">)</span>
</div><div id="l216" class="code_block">            <span class="n">f</span><span class="o">.</span><span class="n">close</span><span class="p">()</span>
</div><div id="l217" class="code_block">    
</div><div id="l218" class="code_block">    <span class="k">def</span> <span class="nf">OnClear</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">event</span><span class="p">):</span>
</div><div id="l219" class="code_block">        <span class="sd">&quot;&quot;&quot;Clear contents of output window.&quot;&quot;&quot;</span>
</div><div id="l220" class="code_block">        <span class="bp">self</span><span class="o">.</span><span class="n">text_ctrl_output</span><span class="o">.</span><span class="n">Clear</span><span class="p">()</span>
</div><div id="l221" class="code_block">    
</div><div id="l222" class="code_block">    <span class="k">def</span> <span class="nf">OnPortSettings</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">event</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span>
</div><div id="l223" class="code_block">        <span class="sd">&quot;&quot;&quot;Show the portsettings dialog. The reader thread is stopped for the</span>
</div><div id="l224" class="code_block"><span class="sd">           settings change.&quot;&quot;&quot;</span>
</div><div id="l225" class="code_block">        <span class="k">if</span> <span class="n">event</span> <span class="ow">is</span> <span class="ow">not</span> <span class="bp">None</span><span class="p">:</span>           <span class="c">#will be none when called on startup</span>
</div><div id="l226" class="code_block">            <span class="bp">self</span><span class="o">.</span><span class="n">StopThread</span><span class="p">()</span>
</div><div id="l227" class="code_block">            <span class="bp">self</span><span class="o">.</span><span class="n">serial</span><span class="o">.</span><span class="n">close</span><span class="p">()</span>
</div><div id="l228" class="code_block">        <span class="n">ok</span> <span class="o">=</span> <span class="bp">False</span>
</div><div id="l229" class="code_block">        <span class="k">while</span> <span class="ow">not</span> <span class="n">ok</span><span class="p">:</span>
</div><div id="l230" class="code_block">            <span class="n">dialog_serial_cfg</span> <span class="o">=</span> <span class="n">wxSerialConfigDialog</span><span class="o">.</span><span class="n">SerialConfigDialog</span><span class="p">(</span><span class="bp">None</span><span class="p">,</span> <span class="o">-</span><span class="mi">1</span><span class="p">,</span> <span class="s">&quot;&quot;</span><span class="p">,</span>
</div><div id="l231" class="code_block">                <span class="n">show</span><span class="o">=</span><span class="n">wxSerialConfigDialog</span><span class="o">.</span><span class="n">SHOW_BAUDRATE</span><span class="o">|</span><span class="n">wxSerialConfigDialog</span><span class="o">.</span><span class="n">SHOW_FORMAT</span><span class="o">|</span><span class="n">wxSerialConfigDialog</span><span class="o">.</span><span class="n">SHOW_FLOW</span><span class="p">,</span>
</div><div id="l232" class="code_block">                <span class="n">serial</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">serial</span>
</div><div id="l233" class="code_block">            <span class="p">)</span>
</div><div id="l234" class="code_block">            <span class="n">result</span> <span class="o">=</span> <span class="n">dialog_serial_cfg</span><span class="o">.</span><span class="n">ShowModal</span><span class="p">()</span>
</div><div id="l235" class="code_block">            <span class="n">dialog_serial_cfg</span><span class="o">.</span><span class="n">Destroy</span><span class="p">()</span>
</div><div id="l236" class="code_block">            <span class="c">#open port if not called on startup, open it on startup and OK too</span>
</div><div id="l237" class="code_block">            <span class="k">if</span> <span class="n">result</span> <span class="o">==</span> <span class="n">wx</span><span class="o">.</span><span class="n">ID_OK</span> <span class="ow">or</span> <span class="n">event</span> <span class="ow">is</span> <span class="ow">not</span> <span class="bp">None</span><span class="p">:</span>
</div><div id="l238" class="code_block">                <span class="k">try</span><span class="p">:</span>
</div><div id="l239" class="code_block">                    <span class="bp">self</span><span class="o">.</span><span class="n">serial</span><span class="o">.</span><span class="n">open</span><span class="p">()</span>
</div><div id="l240" class="code_block">                <span class="k">except</span> <span class="n">serial</span><span class="o">.</span><span class="n">SerialException</span><span class="p">,</span> <span class="n">e</span><span class="p">:</span>
</div><div id="l241" class="code_block">                    <span class="n">dlg</span> <span class="o">=</span> <span class="n">wx</span><span class="o">.</span><span class="n">MessageDialog</span><span class="p">(</span><span class="bp">None</span><span class="p">,</span> <span class="nb">str</span><span class="p">(</span><span class="n">e</span><span class="p">),</span> <span class="s">&quot;Serial Port Error&quot;</span><span class="p">,</span> <span class="n">wx</span><span class="o">.</span><span class="n">OK</span> <span class="o">|</span> <span class="n">wx</span><span class="o">.</span><span class="n">ICON_ERROR</span><span class="p">)</span>
</div><div id="l242" class="code_block">                    <span class="n">dlg</span><span class="o">.</span><span class="n">ShowModal</span><span class="p">()</span>
</div><div id="l243" class="code_block">                    <span class="n">dlg</span><span class="o">.</span><span class="n">Destroy</span><span class="p">()</span>
</div><div id="l244" class="code_block">                <span class="k">else</span><span class="p">:</span>
</div><div id="l245" class="code_block">                    <span class="bp">self</span><span class="o">.</span><span class="n">StartThread</span><span class="p">()</span>
</div><div id="l246" class="code_block">                    <span class="bp">self</span><span class="o">.</span><span class="n">SetTitle</span><span class="p">(</span><span class="s">&quot;Serial Terminal on </span><span class="si">%s</span><span class="s"> [</span><span class="si">%s</span><span class="s">, </span><span class="si">%s%s%s%s%s</span><span class="s">]&quot;</span> <span class="o">%</span> <span class="p">(</span>
</div><div id="l247" class="code_block">                        <span class="bp">self</span><span class="o">.</span><span class="n">serial</span><span class="o">.</span><span class="n">portstr</span><span class="p">,</span>
</div><div id="l248" class="code_block">                        <span class="bp">self</span><span class="o">.</span><span class="n">serial</span><span class="o">.</span><span class="n">baudrate</span><span class="p">,</span>
</div><div id="l249" class="code_block">                        <span class="bp">self</span><span class="o">.</span><span class="n">serial</span><span class="o">.</span><span class="n">bytesize</span><span class="p">,</span>
</div><div id="l250" class="code_block">                        <span class="bp">self</span><span class="o">.</span><span class="n">serial</span><span class="o">.</span><span class="n">parity</span><span class="p">,</span>
</div><div id="l251" class="code_block">                        <span class="bp">self</span><span class="o">.</span><span class="n">serial</span><span class="o">.</span><span class="n">stopbits</span><span class="p">,</span>
</div><div id="l252" class="code_block">                        <span class="bp">self</span><span class="o">.</span><span class="n">serial</span><span class="o">.</span><span class="n">rtscts</span> <span class="ow">and</span> <span class="s">&#39; RTS/CTS&#39;</span> <span class="ow">or</span> <span class="s">&#39;&#39;</span><span class="p">,</span>
</div><div id="l253" class="code_block">                        <span class="bp">self</span><span class="o">.</span><span class="n">serial</span><span class="o">.</span><span class="n">xonxoff</span> <span class="ow">and</span> <span class="s">&#39; Xon/Xoff&#39;</span> <span class="ow">or</span> <span class="s">&#39;&#39;</span><span class="p">,</span>
</div><div id="l254" class="code_block">                        <span class="p">)</span>
</div><div id="l255" class="code_block">                    <span class="p">)</span>
</div><div id="l256" class="code_block">                    <span class="n">ok</span> <span class="o">=</span> <span class="bp">True</span>
</div><div id="l257" class="code_block">            <span class="k">else</span><span class="p">:</span>
</div><div id="l258" class="code_block">                <span class="c">#on startup, dialog aborted</span>
</div><div id="l259" class="code_block">                <span class="bp">self</span><span class="o">.</span><span class="n">alive</span><span class="o">.</span><span class="n">clear</span><span class="p">()</span>
</div><div id="l260" class="code_block">                <span class="n">ok</span> <span class="o">=</span> <span class="bp">True</span>
</div><div id="l261" class="code_block">
</div><div id="l262" class="code_block">    <span class="k">def</span> <span class="nf">OnTermSettings</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">event</span><span class="p">):</span>
</div><div id="l263" class="code_block">        <span class="sd">&quot;&quot;&quot;Menu point Terminal Settings. Show the settings dialog</span>
</div><div id="l264" class="code_block"><span class="sd">           with the current terminal settings&quot;&quot;&quot;</span>
</div><div id="l265" class="code_block">        <span class="n">dialog</span> <span class="o">=</span> <span class="n">TerminalSettingsDialog</span><span class="p">(</span><span class="bp">None</span><span class="p">,</span> <span class="o">-</span><span class="mi">1</span><span class="p">,</span> <span class="s">&quot;&quot;</span><span class="p">,</span> <span class="n">settings</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="p">)</span>
</div><div id="l266" class="code_block">        <span class="n">result</span> <span class="o">=</span> <span class="n">dialog</span><span class="o">.</span><span class="n">ShowModal</span><span class="p">()</span>
</div><div id="l267" class="code_block">        <span class="n">dialog</span><span class="o">.</span><span class="n">Destroy</span><span class="p">()</span>
</div><div id="l268" class="code_block">        
</div><div id="l269" class="code_block">    <span class="k">def</span> <span class="nf">OnKey</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">event</span><span class="p">):</span>
</div><div id="l270" class="code_block">        <span class="sd">&quot;&quot;&quot;Key event handler. if the key is in the ASCII range, write it to the serial port.</span>
</div><div id="l271" class="code_block"><span class="sd">           Newline handling and local echo is also done here.&quot;&quot;&quot;</span>
</div><div id="l272" class="code_block">        <span class="n">code</span> <span class="o">=</span> <span class="n">event</span><span class="o">.</span><span class="n">GetKeyCode</span><span class="p">()</span>
</div><div id="l273" class="code_block">        <span class="k">if</span> <span class="n">code</span> <span class="o">&lt;</span> <span class="mi">256</span><span class="p">:</span>                          <span class="c">#is it printable?</span>
</div><div id="l274" class="code_block">            <span class="k">if</span> <span class="n">code</span> <span class="o">==</span> <span class="mi">13</span><span class="p">:</span>                      <span class="c">#is it a newline? (check for CR which is the RETURN key)</span>
</div><div id="l275" class="code_block">                <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">echo</span><span class="p">:</span>          <span class="c">#do echo if needed</span>
</div><div id="l276" class="code_block">                    <span class="bp">self</span><span class="o">.</span><span class="n">text_ctrl_output</span><span class="o">.</span><span class="n">AppendText</span><span class="p">(</span><span class="s">&#39;</span><span class="se">\n</span><span class="s">&#39;</span><span class="p">)</span>
</div><div id="l277" class="code_block">                <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">newline</span> <span class="o">==</span> <span class="n">NEWLINE_CR</span><span class="p">:</span>
</div><div id="l278" class="code_block">                    <span class="bp">self</span><span class="o">.</span><span class="n">serial</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="s">&#39;</span><span class="se">\r</span><span class="s">&#39;</span><span class="p">)</span>     <span class="c">#send CR</span>
</div><div id="l279" class="code_block">                <span class="k">elif</span> <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">newline</span> <span class="o">==</span> <span class="n">NEWLINE_LF</span><span class="p">:</span>
</div><div id="l280" class="code_block">                    <span class="bp">self</span><span class="o">.</span><span class="n">serial</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="s">&#39;</span><span class="se">\n</span><span class="s">&#39;</span><span class="p">)</span>     <span class="c">#send LF</span>
</div><div id="l281" class="code_block">                <span class="k">elif</span> <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">newline</span> <span class="o">==</span> <span class="n">NEWLINE_CRLF</span><span class="p">:</span>
</div><div id="l282" class="code_block">                    <span class="bp">self</span><span class="o">.</span><span class="n">serial</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="s">&#39;</span><span class="se">\r\n</span><span class="s">&#39;</span><span class="p">)</span>   <span class="c">#send CR+LF</span>
</div><div id="l283" class="code_block">            <span class="k">else</span><span class="p">:</span>
</div><div id="l284" class="code_block">                <span class="n">char</span> <span class="o">=</span> <span class="nb">chr</span><span class="p">(</span><span class="n">code</span><span class="p">)</span>
</div><div id="l285" class="code_block">                <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">echo</span><span class="p">:</span>          <span class="c">#do echo if needed</span>
</div><div id="l286" class="code_block">                    <span class="bp">self</span><span class="o">.</span><span class="n">text_ctrl_output</span><span class="o">.</span><span class="n">WriteText</span><span class="p">(</span><span class="n">char</span><span class="p">)</span>
</div><div id="l287" class="code_block">                <span class="bp">self</span><span class="o">.</span><span class="n">serial</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="n">char</span><span class="p">)</span>         <span class="c">#send the charcater</span>
</div><div id="l288" class="code_block">        <span class="k">else</span><span class="p">:</span>
</div><div id="l289" class="code_block">            <span class="k">print</span> <span class="s">&quot;Extra Key:&quot;</span><span class="p">,</span> <span class="n">code</span>
</div><div id="l290" class="code_block">
</div><div id="l291" class="code_block">    <span class="k">def</span> <span class="nf">OnSerialRead</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">event</span><span class="p">):</span>
</div><div id="l292" class="code_block">        <span class="sd">&quot;&quot;&quot;Handle input from the serial port.&quot;&quot;&quot;</span>
</div><div id="l293" class="code_block">        <span class="n">text</span> <span class="o">=</span> <span class="n">event</span><span class="o">.</span><span class="n">data</span>
</div><div id="l294" class="code_block">        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">unprintable</span><span class="p">:</span>
</div><div id="l295" class="code_block">            <span class="n">text</span> <span class="o">=</span> <span class="s">&#39;&#39;</span><span class="o">.</span><span class="n">join</span><span class="p">([(</span><span class="n">c</span> <span class="o">&gt;=</span> <span class="s">&#39; &#39;</span><span class="p">)</span> <span class="ow">and</span> <span class="n">c</span> <span class="ow">or</span> <span class="s">&#39;&lt;</span><span class="si">%d</span><span class="s">&gt;&#39;</span> <span class="o">%</span> <span class="nb">ord</span><span class="p">(</span><span class="n">c</span><span class="p">)</span>  <span class="k">for</span> <span class="n">c</span> <span class="ow">in</span> <span class="n">text</span><span class="p">])</span>
</div><div id="l296" class="code_block">        <span class="bp">self</span><span class="o">.</span><span class="n">text_ctrl_output</span><span class="o">.</span><span class="n">AppendText</span><span class="p">(</span><span class="n">text</span><span class="p">)</span>
</div><div id="l297" class="code_block">
</div><div id="l298" class="code_block">    <span class="k">def</span> <span class="nf">ComPortThread</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</div><div id="l299" class="code_block">        <span class="sd">&quot;&quot;&quot;Thread that handles the incomming traffic. Does the basic input</span>
</div><div id="l300" class="code_block"><span class="sd">           transformation (newlines) and generates an SerialRxEvent&quot;&quot;&quot;</span>
</div><div id="l301" class="code_block">        <span class="k">while</span> <span class="bp">self</span><span class="o">.</span><span class="n">alive</span><span class="o">.</span><span class="n">isSet</span><span class="p">():</span>               <span class="c">#loop while alive event is true</span>
</div><div id="l302" class="code_block">            <span class="n">text</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">serial</span><span class="o">.</span><span class="n">read</span><span class="p">(</span><span class="mi">1</span><span class="p">)</span>          <span class="c">#read one, with timout</span>
</div><div id="l303" class="code_block">            <span class="k">if</span> <span class="n">text</span><span class="p">:</span>                            <span class="c">#check if not timeout</span>
</div><div id="l304" class="code_block">                <span class="n">n</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">serial</span><span class="o">.</span><span class="n">inWaiting</span><span class="p">()</span>     <span class="c">#look if there is more to read</span>
</div><div id="l305" class="code_block">                <span class="k">if</span> <span class="n">n</span><span class="p">:</span>
</div><div id="l306" class="code_block">                    <span class="n">text</span> <span class="o">=</span> <span class="n">text</span> <span class="o">+</span> <span class="bp">self</span><span class="o">.</span><span class="n">serial</span><span class="o">.</span><span class="n">read</span><span class="p">(</span><span class="n">n</span><span class="p">)</span> <span class="c">#get it</span>
</div><div id="l307" class="code_block">                <span class="c">#newline transformation</span>
</div><div id="l308" class="code_block">                <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">newline</span> <span class="o">==</span> <span class="n">NEWLINE_CR</span><span class="p">:</span>
</div><div id="l309" class="code_block">                    <span class="n">text</span> <span class="o">=</span> <span class="n">text</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="s">&#39;</span><span class="se">\r</span><span class="s">&#39;</span><span class="p">,</span> <span class="s">&#39;</span><span class="se">\n</span><span class="s">&#39;</span><span class="p">)</span>
</div><div id="l310" class="code_block">                <span class="k">elif</span> <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">newline</span> <span class="o">==</span> <span class="n">NEWLINE_LF</span><span class="p">:</span>
</div><div id="l311" class="code_block">                    <span class="k">pass</span>
</div><div id="l312" class="code_block">                <span class="k">elif</span> <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">newline</span> <span class="o">==</span> <span class="n">NEWLINE_CRLF</span><span class="p">:</span>
</div><div id="l313" class="code_block">                    <span class="n">text</span> <span class="o">=</span> <span class="n">text</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="s">&#39;</span><span class="se">\r\n</span><span class="s">&#39;</span><span class="p">,</span> <span class="s">&#39;</span><span class="se">\n</span><span class="s">&#39;</span><span class="p">)</span>
</div><div id="l314" class="code_block">                <span class="n">event</span> <span class="o">=</span> <span class="n">SerialRxEvent</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">GetId</span><span class="p">(),</span> <span class="n">text</span><span class="p">)</span>
</div><div id="l315" class="code_block">                <span class="bp">self</span><span class="o">.</span><span class="n">GetEventHandler</span><span class="p">()</span><span class="o">.</span><span class="n">AddPendingEvent</span><span class="p">(</span><span class="n">event</span><span class="p">)</span>
</div><div id="l316" class="code_block">                <span class="c">#~ self.OnSerialRead(text)         #output text in window</span>
</div><div id="l317" class="code_block">            
</div><div id="l318" class="code_block"><span class="c"># end of class TerminalFrame</span>
</div><div id="l319" class="code_block">
</div><div id="l320" class="code_block">
</div><div id="l321" class="code_block"><span class="k">class</span> <span class="nc">MyApp</span><span class="p">(</span><span class="n">wx</span><span class="o">.</span><span class="n">App</span><span class="p">):</span>
</div><div id="l322" class="code_block">    <span class="k">def</span> <span class="nf">OnInit</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</div><div id="l323" class="code_block">        <span class="n">wx</span><span class="o">.</span><span class="n">InitAllImageHandlers</span><span class="p">()</span>
</div><div id="l324" class="code_block">        <span class="n">frame_terminal</span> <span class="o">=</span> <span class="n">TerminalFrame</span><span class="p">(</span><span class="bp">None</span><span class="p">,</span> <span class="o">-</span><span class="mi">1</span><span class="p">,</span> <span class="s">&quot;&quot;</span><span class="p">)</span>
</div><div id="l325" class="code_block">        <span class="bp">self</span><span class="o">.</span><span class="n">SetTopWindow</span><span class="p">(</span><span class="n">frame_terminal</span><span class="p">)</span>
</div><div id="l326" class="code_block">        <span class="n">frame_terminal</span><span class="o">.</span><span class="n">Show</span><span class="p">(</span><span class="mi">1</span><span class="p">)</span>
</div><div id="l327" class="code_block">        <span class="k">return</span> <span class="mi">1</span>
</div><div id="l328" class="code_block">
</div><div id="l329" class="code_block"><span class="c"># end of class MyApp</span>
</div><div id="l330" class="code_block">
</div><div id="l331" class="code_block"><span class="k">if</span> <span class="n">__name__</span> <span class="o">==</span> <span class="s">&quot;__main__&quot;</span><span class="p">:</span>
</div><div id="l332" class="code_block">    <span class="n">app</span> <span class="o">=</span> <span class="n">MyApp</span><span class="p">(</span><span class="mi">0</span><span class="p">)</span>
</div><div id="l333" class="code_block">    <span class="n">app</span><span class="o">.</span><span class="n">MainLoop</span><span class="p">()</span>
</div></pre></div>
</td></tr></table>
      
    </div>
  

          </div>
			
          
        </div>
      
      </div>
    </section>
      
<footer id="site-footer">
    <div class="wrapper">
        <nav>
            <h5>SourceForge</h5>
            <a href="/about">About</a>
            <a href="/blog/category/sitestatus/">Site Status</a>
            <a href="http://twitter.com/sfnet_ops">@sfnet_ops</a>
            <a id="allura-notice" href="http://allura.apache.org/">
                <p>Powered by</p>
                <p>Apache Allura™</p>
                <img src="http://a.fsdn.com/allura/nf/1433526507/_ew_/theme/sftheme//images/sftheme/logo-black-svg_g.png" />
            </a>
        </nav>
        <nav>
            <h5>Find and Develop Software</h5>
            <a href="/create/">Create a Project</a>
            <a href="/directory/">Software Directory</a>
            <a href="/top">Top Downloaded Projects</a>
        </nav>
        <nav>
            <h5>Community</h5>
            <a href="/blog/">Blog</a>
            <a href="http://twitter.com/sourceforge">@sourceforge</a>
            <a href="/jobs?source=footer">Job Board</a>
            <a href="http://library.slashdotmedia.com/?source=sfnet_footer">Resources</a>
        </nav>
        <nav>
            <h5>Help</h5>
            <a href="http://p.sf.net/sourceforge/docs">Site Documentation</a>
            <a href="/support">Support Request</a>
            <a href="http://p.sf.net/sourceforge/irc">Real-Time Support</a>
        </nav>
    </div>
</footer>
<footer id="site-copyright-footer">
    <div class="wrapper">
        <div id="copyright">
            &copy; 2015 Slashdot Media. All Rights Reserved.<br />
            <div id="dhi-icon"><span class="logo-DHI-alt"></span></div>
            <div id="service-text"><div class="smalltext"> SourceForge is a <a href="http://www.dhigroupinc.com" target="_blank">DHI service</a></div></div>
        </div>
        <nav>
            <a href="http://slashdotmedia.com/terms-of-use">Terms</a>
            <a href="http://slashdotmedia.com/privacy-statement/">Privacy</a>
            <span id='teconsent'></span>
            <a href="http://slashdotmedia.com/opt-out-choices">Opt Out Choices</a>
            <a href="http://slashdotmedia.com">Advertise</a>
            <a href="http://sourceforge.jp/">SourceForge.JP</a>
        </nav>
    </div>
</footer>
    <div id="messages">
        
    </div>
    
    
      <!-- ew:body_js -->

    
      <script type="text/javascript" src="http://a.fsdn.com/allura/nf/1433526507/_ew_/_slim/js?href=allura%2Fjs%2Fjquery.notify.js%3Ballura%2Fjs%2Fmodernizr.js%3Ballura%2Fjs%2Fsylvester.js%3Ballura%2Fjs%2Fpb.transformie.min.js%3Ballura%2Fjs%2Fallura-base.js%3Btheme%2Fsftheme%2Fjs%2Fsftheme%2Fheader.js%3Ballura%2Fjs%2Fmaximize-content.js"></script>
    
      
<!-- /ew:body_js -->

    
    
      <!-- ew:body_js_tail -->

    
      
<!-- /ew:body_js_tail -->

    
    

<script type="text/javascript">(function() {
  $('#access_urls .btn').click(function(evt){
    evt.preventDefault();
    var parent = $(this).parents('.btn-bar');
    $(parent).find('input').val($(this).attr('data-url'));
    $(parent).find('span').text($(this).attr('title')+' access');
    $(this).parent().children('.btn').removeClass('active');
    $(this).addClass('active');
  });
  $('#access_urls .btn').first().click();

  
  var repo_status = document.getElementById('repo_status');
  // The repo_status div will only be present if repo.status != 'ready'
  if (repo_status) {
    $('.spinner').show()
    function check_status() {
        $.get('/p/pyserial/code/status', function(data) {
            if (data.status === 'ready') {
                window.clearInterval(status_checker);
                $('.spinner').hide()
                $('#repo_status h2').html('Repo status: ready. <a href=".">Click here to refresh this page.</a>');
            }
            else {
                $('#repo_status h2 span').html(data.status);
            }
        });
    }
    // Check repo status every 15 seconds
    var status_checker = window.setInterval(check_status, 15000);
    
  }
}());
</script>

<script type="text/javascript">(function() {
  $(window).bind('hashchange', function(e) {
    var hash = window.location.hash.substring(1);
	if ('originalEvent' in e && 'oldURL' in e.originalEvent) {
      $('#' + e.originalEvent.oldURL.split('#')[1]).css('background-color', 'transparent');
	}
    if (hash !== '' && hash.substring(0, 1) === 'l' && !isNaN(hash.substring(1))) {
      $('#' + hash).css('background-color', '#ffff99');
    }
  }).trigger('hashchange');

  var clicks = 0;
  $('.code_block').each(function(index, element) {
    $(element).bind('click', function() {
      // Trick to ignore double and triple clicks
      clicks++;
      if (clicks == 1) {
        setTimeout(function() {
          if (clicks == 1) {
            var hash = window.location.hash.substring(1);
            if (hash !== '' && hash.substring(0, 1) === 'l' && !isNaN(hash.substring(1))) {
              $('#' + hash).css('background-color', 'transparent');
            }
            $(element).css('background-color', '#ffff99');
            window.location.href = '#' + $(element).attr('id');
          };
          clicks = 0;
        }, 500);
      };
    });
  });
}());
</script>

    
      
    
    
    <!-- Google Code for Remarketing tag -->
    <!-- Remarketing tags may not be associated with personally identifiable information or placed on pages related to sensitive categories. For instructions on adding this tag and more information on the above requirements, read the setup guide: google.com/ads/remarketingsetup -->
    <script type="text/javascript">
        /* <![CDATA[ */
        var google_conversion_id = 1002083962;
        var google_conversion_label = "G_uGCOaBlAQQ-qzq3QM";
        var google_custom_params = window.google_tag_params;
        var google_remarketing_only = true;
        /* ]]> */
    </script>
    <script type="text/javascript" src="//www.googleadservices.com/pagead/conversion.js"> </script>
    <script type="text/javascript" src='//consent-st.truste.com/get?name=notice.js&domain=slashdot.org&c=teconsent&text=true'></script>
    <noscript>
      <div style="display:inline;">
        <img height="1" width="1" style="border-style:none;" alt="" src="//googleads.g.doubleclick.net/pagead/viewthroughconversion/1002083962/?value=0&amp;label=G_uGCOaBlAQQ-qzq3QM&amp;guid=ON&amp;script=0"/>
      </div>
    </noscript>

     
      
    
  </body>
</html>
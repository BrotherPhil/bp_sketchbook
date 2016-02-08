<!DOCTYPE html>
<!-- Server: sfn-web-19 -->


  












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
  /trunk/pyserial/examples/rfc2217_server.py
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

      <style>.XqHKsuzxBOyfamxGTpzs { display:none }</style>

    
    
    
    


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
    
  
 rfc2217_server.py

            <!-- actions -->
            <small>
            

    
    <a id="maximize-content" href="#">
      <b data-icon="`" class="ico ico-expand" title="Maximize"> </b> Maximize
    </a>
    <a id="restore-content" href="#">
      <b data-icon="J" class="ico ico-restore" title="Restore"> </b> Restore
    </a>
<a href="/p/pyserial/code/508/log/?path=/trunk/pyserial/examples/rfc2217_server.py">
  <b data-icon="N" class="ico ico-history" title="History"> </b> History
</a>

            </small>
            <!-- /actions -->
          </h2>
		
          <div>
            
  

            
  
    <p><a href="?format=raw">Download this file</a></p>
    <div class="clip grid-19 codebrowser">
      <h3>
        <span class="ico-l"><b data-icon="n" class="ico ico-table"></b> rfc2217_server.py</span>
        &nbsp;&nbsp;
        205 lines (179 with data), 6.7 kB
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
204</pre></div></td><td class="code"><div class="codehilite"><pre><div id="l1" class="code_block"><span class="c">#!/usr/bin/env python</span>
</div><div id="l2" class="code_block">
</div><div id="l3" class="code_block"><span class="c"># (C) 2009 Chris Liechti &lt;cliechti@gmx.net&gt;</span>
</div><div id="l4" class="code_block"><span class="c"># redirect data from a TCP/IP connection to a serial port and vice versa</span>
</div><div id="l5" class="code_block"><span class="c"># using RFC 2217</span>
</div><div id="l6" class="code_block">
</div><div id="l7" class="code_block">
</div><div id="l8" class="code_block"><span class="kn">import</span> <span class="nn">sys</span>
</div><div id="l9" class="code_block"><span class="kn">import</span> <span class="nn">os</span>
</div><div id="l10" class="code_block"><span class="kn">import</span> <span class="nn">threading</span>
</div><div id="l11" class="code_block"><span class="kn">import</span> <span class="nn">time</span>
</div><div id="l12" class="code_block"><span class="kn">import</span> <span class="nn">socket</span>
</div><div id="l13" class="code_block"><span class="kn">import</span> <span class="nn">serial</span>
</div><div id="l14" class="code_block"><span class="kn">import</span> <span class="nn">serial.rfc2217</span>
</div><div id="l15" class="code_block"><span class="kn">import</span> <span class="nn">logging</span>
</div><div id="l16" class="code_block">
</div><div id="l17" class="code_block"><span class="k">class</span> <span class="nc">Redirector</span><span class="p">:</span>
</div><div id="l18" class="code_block">    <span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">serial_instance</span><span class="p">,</span> <span class="n">socket</span><span class="p">,</span> <span class="n">debug</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span>
</div><div id="l19" class="code_block">        <span class="bp">self</span><span class="o">.</span><span class="n">serial</span> <span class="o">=</span> <span class="n">serial_instance</span>
</div><div id="l20" class="code_block">        <span class="bp">self</span><span class="o">.</span><span class="n">socket</span> <span class="o">=</span> <span class="n">socket</span>
</div><div id="l21" class="code_block">        <span class="bp">self</span><span class="o">.</span><span class="n">_write_lock</span> <span class="o">=</span> <span class="n">threading</span><span class="o">.</span><span class="n">Lock</span><span class="p">()</span>
</div><div id="l22" class="code_block">        <span class="bp">self</span><span class="o">.</span><span class="n">rfc2217</span> <span class="o">=</span> <span class="n">serial</span><span class="o">.</span><span class="n">rfc2217</span><span class="o">.</span><span class="n">PortManager</span><span class="p">(</span>
</div><div id="l23" class="code_block">            <span class="bp">self</span><span class="o">.</span><span class="n">serial</span><span class="p">,</span>
</div><div id="l24" class="code_block">            <span class="bp">self</span><span class="p">,</span>
</div><div id="l25" class="code_block">            <span class="n">logger</span> <span class="o">=</span> <span class="p">(</span><span class="n">debug</span> <span class="ow">and</span> <span class="n">logging</span><span class="o">.</span><span class="n">getLogger</span><span class="p">(</span><span class="s">&#39;rfc2217.server&#39;</span><span class="p">))</span>
</div><div id="l26" class="code_block">            <span class="p">)</span>
</div><div id="l27" class="code_block">        <span class="bp">self</span><span class="o">.</span><span class="n">log</span> <span class="o">=</span> <span class="n">logging</span><span class="o">.</span><span class="n">getLogger</span><span class="p">(</span><span class="s">&#39;redirector&#39;</span><span class="p">)</span>
</div><div id="l28" class="code_block">
</div><div id="l29" class="code_block">    <span class="k">def</span> <span class="nf">statusline_poller</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</div><div id="l30" class="code_block">        <span class="bp">self</span><span class="o">.</span><span class="n">log</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="s">&#39;status line poll thread started&#39;</span><span class="p">)</span>
</div><div id="l31" class="code_block">        <span class="k">while</span> <span class="bp">self</span><span class="o">.</span><span class="n">alive</span><span class="p">:</span>
</div><div id="l32" class="code_block">            <span class="n">time</span><span class="o">.</span><span class="n">sleep</span><span class="p">(</span><span class="mi">1</span><span class="p">)</span>
</div><div id="l33" class="code_block">            <span class="bp">self</span><span class="o">.</span><span class="n">rfc2217</span><span class="o">.</span><span class="n">check_modem_lines</span><span class="p">()</span>
</div><div id="l34" class="code_block">        <span class="bp">self</span><span class="o">.</span><span class="n">log</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="s">&#39;status line poll thread terminated&#39;</span><span class="p">)</span>
</div><div id="l35" class="code_block">
</div><div id="l36" class="code_block">    <span class="k">def</span> <span class="nf">shortcut</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</div><div id="l37" class="code_block">        <span class="sd">&quot;&quot;&quot;connect the serial port to the TCP port by copying everything</span>
</div><div id="l38" class="code_block"><span class="sd">           from one side to the other&quot;&quot;&quot;</span>
</div><div id="l39" class="code_block">        <span class="bp">self</span><span class="o">.</span><span class="n">alive</span> <span class="o">=</span> <span class="bp">True</span>
</div><div id="l40" class="code_block">        <span class="bp">self</span><span class="o">.</span><span class="n">thread_read</span> <span class="o">=</span> <span class="n">threading</span><span class="o">.</span><span class="n">Thread</span><span class="p">(</span><span class="n">target</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">reader</span><span class="p">)</span>
</div><div id="l41" class="code_block">        <span class="bp">self</span><span class="o">.</span><span class="n">thread_read</span><span class="o">.</span><span class="n">setDaemon</span><span class="p">(</span><span class="bp">True</span><span class="p">)</span>
</div><div id="l42" class="code_block">        <span class="bp">self</span><span class="o">.</span><span class="n">thread_read</span><span class="o">.</span><span class="n">setName</span><span class="p">(</span><span class="s">&#39;serial-&gt;socket&#39;</span><span class="p">)</span>
</div><div id="l43" class="code_block">        <span class="bp">self</span><span class="o">.</span><span class="n">thread_read</span><span class="o">.</span><span class="n">start</span><span class="p">()</span>
</div><div id="l44" class="code_block">        <span class="bp">self</span><span class="o">.</span><span class="n">thread_poll</span> <span class="o">=</span> <span class="n">threading</span><span class="o">.</span><span class="n">Thread</span><span class="p">(</span><span class="n">target</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">statusline_poller</span><span class="p">)</span>
</div><div id="l45" class="code_block">        <span class="bp">self</span><span class="o">.</span><span class="n">thread_poll</span><span class="o">.</span><span class="n">setDaemon</span><span class="p">(</span><span class="bp">True</span><span class="p">)</span>
</div><div id="l46" class="code_block">        <span class="bp">self</span><span class="o">.</span><span class="n">thread_poll</span><span class="o">.</span><span class="n">setName</span><span class="p">(</span><span class="s">&#39;status line poll&#39;</span><span class="p">)</span>
</div><div id="l47" class="code_block">        <span class="bp">self</span><span class="o">.</span><span class="n">thread_poll</span><span class="o">.</span><span class="n">start</span><span class="p">()</span>
</div><div id="l48" class="code_block">        <span class="bp">self</span><span class="o">.</span><span class="n">writer</span><span class="p">()</span>
</div><div id="l49" class="code_block">
</div><div id="l50" class="code_block">    <span class="k">def</span> <span class="nf">reader</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</div><div id="l51" class="code_block">        <span class="sd">&quot;&quot;&quot;loop forever and copy serial-&gt;socket&quot;&quot;&quot;</span>
</div><div id="l52" class="code_block">        <span class="bp">self</span><span class="o">.</span><span class="n">log</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="s">&#39;reader thread started&#39;</span><span class="p">)</span>
</div><div id="l53" class="code_block">        <span class="k">while</span> <span class="bp">self</span><span class="o">.</span><span class="n">alive</span><span class="p">:</span>
</div><div id="l54" class="code_block">            <span class="k">try</span><span class="p">:</span>
</div><div id="l55" class="code_block">                <span class="n">data</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">serial</span><span class="o">.</span><span class="n">read</span><span class="p">(</span><span class="mi">1</span><span class="p">)</span>              <span class="c"># read one, blocking</span>
</div><div id="l56" class="code_block">                <span class="n">n</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">serial</span><span class="o">.</span><span class="n">inWaiting</span><span class="p">()</span>             <span class="c"># look if there is more</span>
</div><div id="l57" class="code_block">                <span class="k">if</span> <span class="n">n</span><span class="p">:</span>
</div><div id="l58" class="code_block">                    <span class="n">data</span> <span class="o">=</span> <span class="n">data</span> <span class="o">+</span> <span class="bp">self</span><span class="o">.</span><span class="n">serial</span><span class="o">.</span><span class="n">read</span><span class="p">(</span><span class="n">n</span><span class="p">)</span>   <span class="c"># and get as much as possible</span>
</div><div id="l59" class="code_block">                <span class="k">if</span> <span class="n">data</span><span class="p">:</span>
</div><div id="l60" class="code_block">                    <span class="c"># escape outgoing data when needed (Telnet IAC (0xff) character)</span>
</div><div id="l61" class="code_block">                    <span class="n">data</span> <span class="o">=</span> <span class="n">serial</span><span class="o">.</span><span class="n">to_bytes</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">rfc2217</span><span class="o">.</span><span class="n">escape</span><span class="p">(</span><span class="n">data</span><span class="p">))</span>
</div><div id="l62" class="code_block">                    <span class="bp">self</span><span class="o">.</span><span class="n">_write_lock</span><span class="o">.</span><span class="n">acquire</span><span class="p">()</span>
</div><div id="l63" class="code_block">                    <span class="k">try</span><span class="p">:</span>
</div><div id="l64" class="code_block">                        <span class="bp">self</span><span class="o">.</span><span class="n">socket</span><span class="o">.</span><span class="n">sendall</span><span class="p">(</span><span class="n">data</span><span class="p">)</span>       <span class="c"># send it over TCP</span>
</div><div id="l65" class="code_block">                    <span class="k">finally</span><span class="p">:</span>
</div><div id="l66" class="code_block">                        <span class="bp">self</span><span class="o">.</span><span class="n">_write_lock</span><span class="o">.</span><span class="n">release</span><span class="p">()</span>
</div><div id="l67" class="code_block">            <span class="k">except</span> <span class="n">socket</span><span class="o">.</span><span class="n">error</span><span class="p">,</span> <span class="n">msg</span><span class="p">:</span>
</div><div id="l68" class="code_block">                <span class="bp">self</span><span class="o">.</span><span class="n">log</span><span class="o">.</span><span class="n">error</span><span class="p">(</span><span class="s">&#39;</span><span class="si">%s</span><span class="s">&#39;</span> <span class="o">%</span> <span class="p">(</span><span class="n">msg</span><span class="p">,))</span>
</div><div id="l69" class="code_block">                <span class="c"># probably got disconnected</span>
</div><div id="l70" class="code_block">                <span class="k">break</span>
</div><div id="l71" class="code_block">        <span class="bp">self</span><span class="o">.</span><span class="n">alive</span> <span class="o">=</span> <span class="bp">False</span>
</div><div id="l72" class="code_block">        <span class="bp">self</span><span class="o">.</span><span class="n">log</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="s">&#39;reader thread terminated&#39;</span><span class="p">)</span>
</div><div id="l73" class="code_block">
</div><div id="l74" class="code_block">    <span class="k">def</span> <span class="nf">write</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">data</span><span class="p">):</span>
</div><div id="l75" class="code_block">        <span class="sd">&quot;&quot;&quot;thread safe socket write with no data escaping. used to send telnet stuff&quot;&quot;&quot;</span>
</div><div id="l76" class="code_block">        <span class="bp">self</span><span class="o">.</span><span class="n">_write_lock</span><span class="o">.</span><span class="n">acquire</span><span class="p">()</span>
</div><div id="l77" class="code_block">        <span class="k">try</span><span class="p">:</span>
</div><div id="l78" class="code_block">            <span class="bp">self</span><span class="o">.</span><span class="n">socket</span><span class="o">.</span><span class="n">sendall</span><span class="p">(</span><span class="n">data</span><span class="p">)</span>
</div><div id="l79" class="code_block">        <span class="k">finally</span><span class="p">:</span>
</div><div id="l80" class="code_block">            <span class="bp">self</span><span class="o">.</span><span class="n">_write_lock</span><span class="o">.</span><span class="n">release</span><span class="p">()</span>
</div><div id="l81" class="code_block">
</div><div id="l82" class="code_block">    <span class="k">def</span> <span class="nf">writer</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</div><div id="l83" class="code_block">        <span class="sd">&quot;&quot;&quot;loop forever and copy socket-&gt;serial&quot;&quot;&quot;</span>
</div><div id="l84" class="code_block">        <span class="k">while</span> <span class="bp">self</span><span class="o">.</span><span class="n">alive</span><span class="p">:</span>
</div><div id="l85" class="code_block">            <span class="k">try</span><span class="p">:</span>
</div><div id="l86" class="code_block">                <span class="n">data</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">socket</span><span class="o">.</span><span class="n">recv</span><span class="p">(</span><span class="mi">1024</span><span class="p">)</span>
</div><div id="l87" class="code_block">                <span class="k">if</span> <span class="ow">not</span> <span class="n">data</span><span class="p">:</span>
</div><div id="l88" class="code_block">                    <span class="k">break</span>
</div><div id="l89" class="code_block">                <span class="bp">self</span><span class="o">.</span><span class="n">serial</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="n">serial</span><span class="o">.</span><span class="n">to_bytes</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">rfc2217</span><span class="o">.</span><span class="n">filter</span><span class="p">(</span><span class="n">data</span><span class="p">)))</span>
</div><div id="l90" class="code_block">            <span class="k">except</span> <span class="n">socket</span><span class="o">.</span><span class="n">error</span><span class="p">,</span> <span class="n">msg</span><span class="p">:</span>
</div><div id="l91" class="code_block">                <span class="bp">self</span><span class="o">.</span><span class="n">log</span><span class="o">.</span><span class="n">error</span><span class="p">(</span><span class="s">&#39;</span><span class="si">%s</span><span class="s">&#39;</span> <span class="o">%</span> <span class="p">(</span><span class="n">msg</span><span class="p">,))</span>
</div><div id="l92" class="code_block">                <span class="c"># probably got disconnected</span>
</div><div id="l93" class="code_block">                <span class="k">break</span>
</div><div id="l94" class="code_block">        <span class="bp">self</span><span class="o">.</span><span class="n">stop</span><span class="p">()</span>
</div><div id="l95" class="code_block">
</div><div id="l96" class="code_block">    <span class="k">def</span> <span class="nf">stop</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</div><div id="l97" class="code_block">        <span class="sd">&quot;&quot;&quot;Stop copying&quot;&quot;&quot;</span>
</div><div id="l98" class="code_block">        <span class="bp">self</span><span class="o">.</span><span class="n">log</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="s">&#39;stopping&#39;</span><span class="p">)</span>
</div><div id="l99" class="code_block">        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">alive</span><span class="p">:</span>
</div><div id="l100" class="code_block">            <span class="bp">self</span><span class="o">.</span><span class="n">alive</span> <span class="o">=</span> <span class="bp">False</span>
</div><div id="l101" class="code_block">            <span class="bp">self</span><span class="o">.</span><span class="n">thread_read</span><span class="o">.</span><span class="n">join</span><span class="p">()</span>
</div><div id="l102" class="code_block">            <span class="bp">self</span><span class="o">.</span><span class="n">thread_poll</span><span class="o">.</span><span class="n">join</span><span class="p">()</span>
</div><div id="l103" class="code_block">
</div><div id="l104" class="code_block">
</div><div id="l105" class="code_block"><span class="k">if</span> <span class="n">__name__</span> <span class="o">==</span> <span class="s">&#39;__main__&#39;</span><span class="p">:</span>
</div><div id="l106" class="code_block">    <span class="kn">import</span> <span class="nn">optparse</span>
</div><div id="l107" class="code_block">
</div><div id="l108" class="code_block">    <span class="n">parser</span> <span class="o">=</span> <span class="n">optparse</span><span class="o">.</span><span class="n">OptionParser</span><span class="p">(</span>
</div><div id="l109" class="code_block">        <span class="n">usage</span> <span class="o">=</span> <span class="s">&quot;%prog [options] port&quot;</span><span class="p">,</span>
</div><div id="l110" class="code_block">        <span class="n">description</span> <span class="o">=</span> <span class="s">&quot;RFC 2217 Serial to Network (TCP/IP) redirector.&quot;</span><span class="p">,</span>
</div><div id="l111" class="code_block">        <span class="n">epilog</span> <span class="o">=</span> <span class="s">&quot;&quot;&quot;</span><span class="se">\</span>
</div><div id="l112" class="code_block"><span class="s">NOTE: no security measures are implemented. Anyone can remotely connect</span>
</div><div id="l113" class="code_block"><span class="s">to this service over the network.</span>
</div><div id="l114" class="code_block">
</div><div id="l115" class="code_block"><span class="s">Only one connection at once is supported. When the connection is terminated</span>
</div><div id="l116" class="code_block"><span class="s">it waits for the next connect.</span>
</div><div id="l117" class="code_block"><span class="s">&quot;&quot;&quot;</span><span class="p">)</span>
</div><div id="l118" class="code_block">
</div><div id="l119" class="code_block">    <span class="n">parser</span><span class="o">.</span><span class="n">add_option</span><span class="p">(</span><span class="s">&quot;-p&quot;</span><span class="p">,</span> <span class="s">&quot;--localport&quot;</span><span class="p">,</span>
</div><div id="l120" class="code_block">        <span class="n">dest</span> <span class="o">=</span> <span class="s">&quot;local_port&quot;</span><span class="p">,</span>
</div><div id="l121" class="code_block">        <span class="n">action</span> <span class="o">=</span> <span class="s">&quot;store&quot;</span><span class="p">,</span>
</div><div id="l122" class="code_block">        <span class="nb">type</span> <span class="o">=</span> <span class="s">&#39;int&#39;</span><span class="p">,</span>
</div><div id="l123" class="code_block">        <span class="n">help</span> <span class="o">=</span> <span class="s">&quot;local TCP port&quot;</span><span class="p">,</span>
</div><div id="l124" class="code_block">        <span class="n">default</span> <span class="o">=</span> <span class="mi">2217</span>
</div><div id="l125" class="code_block">    <span class="p">)</span>
</div><div id="l126" class="code_block">
</div><div id="l127" class="code_block">    <span class="n">parser</span><span class="o">.</span><span class="n">add_option</span><span class="p">(</span><span class="s">&quot;-v&quot;</span><span class="p">,</span> <span class="s">&quot;--verbose&quot;</span><span class="p">,</span>
</div><div id="l128" class="code_block">        <span class="n">dest</span> <span class="o">=</span> <span class="s">&quot;verbosity&quot;</span><span class="p">,</span>
</div><div id="l129" class="code_block">        <span class="n">action</span> <span class="o">=</span> <span class="s">&quot;count&quot;</span><span class="p">,</span>
</div><div id="l130" class="code_block">        <span class="n">help</span> <span class="o">=</span> <span class="s">&quot;print more diagnostic messages (option can be given multiple times)&quot;</span><span class="p">,</span>
</div><div id="l131" class="code_block">        <span class="n">default</span> <span class="o">=</span> <span class="mi">0</span>
</div><div id="l132" class="code_block">    <span class="p">)</span>
</div><div id="l133" class="code_block">
</div><div id="l134" class="code_block">    <span class="p">(</span><span class="n">options</span><span class="p">,</span> <span class="n">args</span><span class="p">)</span> <span class="o">=</span> <span class="n">parser</span><span class="o">.</span><span class="n">parse_args</span><span class="p">()</span>
</div><div id="l135" class="code_block">
</div><div id="l136" class="code_block">    <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">args</span><span class="p">)</span> <span class="o">!=</span> <span class="mi">1</span><span class="p">:</span>
</div><div id="l137" class="code_block">        <span class="n">parser</span><span class="o">.</span><span class="n">error</span><span class="p">(</span><span class="s">&#39;serial port name required as argument&#39;</span><span class="p">)</span>
</div><div id="l138" class="code_block">
</div><div id="l139" class="code_block">    <span class="k">if</span> <span class="n">options</span><span class="o">.</span><span class="n">verbosity</span> <span class="o">&gt;</span> <span class="mi">3</span><span class="p">:</span>
</div><div id="l140" class="code_block">        <span class="n">options</span><span class="o">.</span><span class="n">verbosity</span> <span class="o">=</span> <span class="mi">3</span>
</div><div id="l141" class="code_block">    <span class="n">level</span> <span class="o">=</span> <span class="p">(</span>
</div><div id="l142" class="code_block">        <span class="n">logging</span><span class="o">.</span><span class="n">WARNING</span><span class="p">,</span>
</div><div id="l143" class="code_block">        <span class="n">logging</span><span class="o">.</span><span class="n">INFO</span><span class="p">,</span>
</div><div id="l144" class="code_block">        <span class="n">logging</span><span class="o">.</span><span class="n">DEBUG</span><span class="p">,</span>
</div><div id="l145" class="code_block">        <span class="n">logging</span><span class="o">.</span><span class="n">NOTSET</span><span class="p">,</span>
</div><div id="l146" class="code_block">        <span class="p">)[</span><span class="n">options</span><span class="o">.</span><span class="n">verbosity</span><span class="p">]</span>
</div><div id="l147" class="code_block">    <span class="n">logging</span><span class="o">.</span><span class="n">basicConfig</span><span class="p">(</span><span class="n">level</span><span class="o">=</span><span class="n">logging</span><span class="o">.</span><span class="n">INFO</span><span class="p">)</span>
</div><div id="l148" class="code_block">    <span class="n">logging</span><span class="o">.</span><span class="n">getLogger</span><span class="p">(</span><span class="s">&#39;root&#39;</span><span class="p">)</span><span class="o">.</span><span class="n">setLevel</span><span class="p">(</span><span class="n">logging</span><span class="o">.</span><span class="n">INFO</span><span class="p">)</span>
</div><div id="l149" class="code_block">    <span class="n">logging</span><span class="o">.</span><span class="n">getLogger</span><span class="p">(</span><span class="s">&#39;rfc2217&#39;</span><span class="p">)</span><span class="o">.</span><span class="n">setLevel</span><span class="p">(</span><span class="n">level</span><span class="p">)</span>
</div><div id="l150" class="code_block">
</div><div id="l151" class="code_block">    <span class="c"># connect to serial port</span>
</div><div id="l152" class="code_block">    <span class="n">ser</span> <span class="o">=</span> <span class="n">serial</span><span class="o">.</span><span class="n">Serial</span><span class="p">()</span>
</div><div id="l153" class="code_block">    <span class="n">ser</span><span class="o">.</span><span class="n">port</span>     <span class="o">=</span> <span class="n">args</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>
</div><div id="l154" class="code_block">    <span class="n">ser</span><span class="o">.</span><span class="n">timeout</span>  <span class="o">=</span> <span class="mi">3</span>     <span class="c"># required so that the reader thread can exit</span>
</div><div id="l155" class="code_block">
</div><div id="l156" class="code_block">    <span class="n">logging</span><span class="o">.</span><span class="n">info</span><span class="p">(</span><span class="s">&quot;RFC 2217 TCP/IP to Serial redirector - type Ctrl-C / BREAK to quit&quot;</span><span class="p">)</span>
</div><div id="l157" class="code_block">
</div><div id="l158" class="code_block">    <span class="k">try</span><span class="p">:</span>
</div><div id="l159" class="code_block">        <span class="n">ser</span><span class="o">.</span><span class="n">open</span><span class="p">()</span>
</div><div id="l160" class="code_block">    <span class="k">except</span> <span class="n">serial</span><span class="o">.</span><span class="n">SerialException</span><span class="p">,</span> <span class="n">e</span><span class="p">:</span>
</div><div id="l161" class="code_block">        <span class="n">logging</span><span class="o">.</span><span class="n">error</span><span class="p">(</span><span class="s">&quot;Could not open serial port </span><span class="si">%s</span><span class="s">: </span><span class="si">%s</span><span class="s">&quot;</span> <span class="o">%</span> <span class="p">(</span><span class="n">ser</span><span class="o">.</span><span class="n">portstr</span><span class="p">,</span> <span class="n">e</span><span class="p">))</span>
</div><div id="l162" class="code_block">        <span class="n">sys</span><span class="o">.</span><span class="n">exit</span><span class="p">(</span><span class="mi">1</span><span class="p">)</span>
</div><div id="l163" class="code_block">
</div><div id="l164" class="code_block">    <span class="n">logging</span><span class="o">.</span><span class="n">info</span><span class="p">(</span><span class="s">&quot;Serving serial port: </span><span class="si">%s</span><span class="s">&quot;</span> <span class="o">%</span> <span class="p">(</span><span class="n">ser</span><span class="o">.</span><span class="n">portstr</span><span class="p">,))</span>
</div><div id="l165" class="code_block">    <span class="n">settings</span> <span class="o">=</span> <span class="n">ser</span><span class="o">.</span><span class="n">getSettingsDict</span><span class="p">()</span>
</div><div id="l166" class="code_block">    <span class="c"># reset control line as no _remote_ &quot;terminal&quot; has been connected yet</span>
</div><div id="l167" class="code_block">    <span class="n">ser</span><span class="o">.</span><span class="n">setDTR</span><span class="p">(</span><span class="bp">False</span><span class="p">)</span>
</div><div id="l168" class="code_block">    <span class="n">ser</span><span class="o">.</span><span class="n">setRTS</span><span class="p">(</span><span class="bp">False</span><span class="p">)</span>
</div><div id="l169" class="code_block">
</div><div id="l170" class="code_block">    <span class="n">srv</span> <span class="o">=</span> <span class="n">socket</span><span class="o">.</span><span class="n">socket</span><span class="p">(</span><span class="n">socket</span><span class="o">.</span><span class="n">AF_INET</span><span class="p">,</span> <span class="n">socket</span><span class="o">.</span><span class="n">SOCK_STREAM</span><span class="p">)</span>
</div><div id="l171" class="code_block">    <span class="n">srv</span><span class="o">.</span><span class="n">setsockopt</span><span class="p">(</span><span class="n">socket</span><span class="o">.</span><span class="n">SOL_SOCKET</span><span class="p">,</span> <span class="n">socket</span><span class="o">.</span><span class="n">SO_REUSEADDR</span><span class="p">,</span> <span class="mi">1</span><span class="p">)</span>
</div><div id="l172" class="code_block">    <span class="n">srv</span><span class="o">.</span><span class="n">bind</span><span class="p">(</span> <span class="p">(</span><span class="s">&#39;&#39;</span><span class="p">,</span> <span class="n">options</span><span class="o">.</span><span class="n">local_port</span><span class="p">)</span> <span class="p">)</span>
</div><div id="l173" class="code_block">    <span class="n">srv</span><span class="o">.</span><span class="n">listen</span><span class="p">(</span><span class="mi">1</span><span class="p">)</span>
</div><div id="l174" class="code_block">    <span class="n">logging</span><span class="o">.</span><span class="n">info</span><span class="p">(</span><span class="s">&quot;TCP/IP port: </span><span class="si">%s</span><span class="s">&quot;</span> <span class="o">%</span> <span class="p">(</span><span class="n">options</span><span class="o">.</span><span class="n">local_port</span><span class="p">,))</span>
</div><div id="l175" class="code_block">    <span class="k">while</span> <span class="bp">True</span><span class="p">:</span>
</div><div id="l176" class="code_block">        <span class="k">try</span><span class="p">:</span>
</div><div id="l177" class="code_block">            <span class="n">connection</span><span class="p">,</span> <span class="n">addr</span> <span class="o">=</span> <span class="n">srv</span><span class="o">.</span><span class="n">accept</span><span class="p">()</span>
</div><div id="l178" class="code_block">            <span class="n">logging</span><span class="o">.</span><span class="n">info</span><span class="p">(</span><span class="s">&#39;Connected by </span><span class="si">%s</span><span class="s">:</span><span class="si">%s</span><span class="s">&#39;</span> <span class="o">%</span> <span class="p">(</span><span class="n">addr</span><span class="p">[</span><span class="mi">0</span><span class="p">],</span> <span class="n">addr</span><span class="p">[</span><span class="mi">1</span><span class="p">]))</span>
</div><div id="l179" class="code_block">            <span class="n">connection</span><span class="o">.</span><span class="n">setsockopt</span><span class="p">(</span> <span class="n">socket</span><span class="o">.</span><span class="n">IPPROTO_TCP</span><span class="p">,</span> <span class="n">socket</span><span class="o">.</span><span class="n">TCP_NODELAY</span><span class="p">,</span> <span class="mi">1</span><span class="p">)</span>
</div><div id="l180" class="code_block">            <span class="n">ser</span><span class="o">.</span><span class="n">setRTS</span><span class="p">(</span><span class="bp">True</span><span class="p">)</span>
</div><div id="l181" class="code_block">            <span class="n">ser</span><span class="o">.</span><span class="n">setDTR</span><span class="p">(</span><span class="bp">True</span><span class="p">)</span>
</div><div id="l182" class="code_block">            <span class="c"># enter network &lt;-&gt; serial loop</span>
</div><div id="l183" class="code_block">            <span class="n">r</span> <span class="o">=</span> <span class="n">Redirector</span><span class="p">(</span>
</div><div id="l184" class="code_block">                <span class="n">ser</span><span class="p">,</span>
</div><div id="l185" class="code_block">                <span class="n">connection</span><span class="p">,</span>
</div><div id="l186" class="code_block">                <span class="n">options</span><span class="o">.</span><span class="n">verbosity</span> <span class="o">&gt;</span> <span class="mi">0</span>
</div><div id="l187" class="code_block">            <span class="p">)</span>
</div><div id="l188" class="code_block">            <span class="k">try</span><span class="p">:</span>
</div><div id="l189" class="code_block">                <span class="n">r</span><span class="o">.</span><span class="n">shortcut</span><span class="p">()</span>
</div><div id="l190" class="code_block">            <span class="k">finally</span><span class="p">:</span>
</div><div id="l191" class="code_block">                <span class="n">logging</span><span class="o">.</span><span class="n">info</span><span class="p">(</span><span class="s">&#39;Disconnected&#39;</span><span class="p">)</span>
</div><div id="l192" class="code_block">                <span class="n">r</span><span class="o">.</span><span class="n">stop</span><span class="p">()</span>
</div><div id="l193" class="code_block">                <span class="n">connection</span><span class="o">.</span><span class="n">close</span><span class="p">()</span>
</div><div id="l194" class="code_block">                <span class="n">ser</span><span class="o">.</span><span class="n">setDTR</span><span class="p">(</span><span class="bp">False</span><span class="p">)</span>
</div><div id="l195" class="code_block">                <span class="n">ser</span><span class="o">.</span><span class="n">setRTS</span><span class="p">(</span><span class="bp">False</span><span class="p">)</span>
</div><div id="l196" class="code_block">            <span class="c"># Restore port settings (may have been changed by RFC 2217 capable</span>
</div><div id="l197" class="code_block">            <span class="c"># client)</span>
</div><div id="l198" class="code_block">            <span class="n">ser</span><span class="o">.</span><span class="n">applySettingsDict</span><span class="p">(</span><span class="n">settings</span><span class="p">)</span>
</div><div id="l199" class="code_block">        <span class="k">except</span> <span class="ne">KeyboardInterrupt</span><span class="p">:</span>
</div><div id="l200" class="code_block">            <span class="k">break</span>
</div><div id="l201" class="code_block">        <span class="k">except</span> <span class="n">socket</span><span class="o">.</span><span class="n">error</span><span class="p">,</span> <span class="n">msg</span><span class="p">:</span>
</div><div id="l202" class="code_block">            <span class="n">logging</span><span class="o">.</span><span class="n">error</span><span class="p">(</span><span class="s">&#39;</span><span class="si">%s</span><span class="s">&#39;</span> <span class="o">%</span> <span class="p">(</span><span class="n">msg</span><span class="p">,))</span>
</div><div id="l203" class="code_block">
</div><div id="l204" class="code_block">    <span class="n">logging</span><span class="o">.</span><span class="n">info</span><span class="p">(</span><span class="s">&#39;--- exit ---&#39;</span><span class="p">)</span>
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
<!DOCTYPE html>
<!-- Server: sfn-web-2 -->


  












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
  /trunk/pyserial/serial/tools/miniterm.py
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

      <style>.XbjGWcwFpWnoXvthdOpHrTZmPnc { display:none }</style>

    
    
    
    


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

  
  
    <a href="./../../../">trunk</a> /
    
  
    <a href="./../../">pyserial</a> /
    
  
    <a href="./../">serial</a> /
    
  
    <a href="./">tools</a> /
    
  
 miniterm.py

            <!-- actions -->
            <small>
            

    
    <a id="maximize-content" href="#">
      <b data-icon="`" class="ico ico-expand" title="Maximize"> </b> Maximize
    </a>
    <a id="restore-content" href="#">
      <b data-icon="J" class="ico ico-restore" title="Restore"> </b> Restore
    </a>
<a href="/p/pyserial/code/508/log/?path=/trunk/pyserial/serial/tools/miniterm.py">
  <b data-icon="N" class="ico ico-history" title="History"> </b> History
</a>

            </small>
            <!-- /actions -->
          </h2>
		
          <div>
            
  

            
  
    <p><a href="?format=raw">Download this file</a></p>
    <div class="clip grid-19 codebrowser">
      <h3>
        <span class="ico-l"><b data-icon="n" class="ico ico-table"></b> miniterm.py</span>
        &nbsp;&nbsp;
        695 lines (612 with data), 27.5 kB
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
333
334
335
336
337
338
339
340
341
342
343
344
345
346
347
348
349
350
351
352
353
354
355
356
357
358
359
360
361
362
363
364
365
366
367
368
369
370
371
372
373
374
375
376
377
378
379
380
381
382
383
384
385
386
387
388
389
390
391
392
393
394
395
396
397
398
399
400
401
402
403
404
405
406
407
408
409
410
411
412
413
414
415
416
417
418
419
420
421
422
423
424
425
426
427
428
429
430
431
432
433
434
435
436
437
438
439
440
441
442
443
444
445
446
447
448
449
450
451
452
453
454
455
456
457
458
459
460
461
462
463
464
465
466
467
468
469
470
471
472
473
474
475
476
477
478
479
480
481
482
483
484
485
486
487
488
489
490
491
492
493
494
495
496
497
498
499
500
501
502
503
504
505
506
507
508
509
510
511
512
513
514
515
516
517
518
519
520
521
522
523
524
525
526
527
528
529
530
531
532
533
534
535
536
537
538
539
540
541
542
543
544
545
546
547
548
549
550
551
552
553
554
555
556
557
558
559
560
561
562
563
564
565
566
567
568
569
570
571
572
573
574
575
576
577
578
579
580
581
582
583
584
585
586
587
588
589
590
591
592
593
594
595
596
597
598
599
600
601
602
603
604
605
606
607
608
609
610
611
612
613
614
615
616
617
618
619
620
621
622
623
624
625
626
627
628
629
630
631
632
633
634
635
636
637
638
639
640
641
642
643
644
645
646
647
648
649
650
651
652
653
654
655
656
657
658
659
660
661
662
663
664
665
666
667
668
669
670
671
672
673
674
675
676
677
678
679
680
681
682
683
684
685
686
687
688
689
690
691
692
693
694</pre></div></td><td class="code"><div class="codehilite"><pre><div id="l1" class="code_block"><span class="c">#!/usr/bin/env python</span>
</div><div id="l2" class="code_block">
</div><div id="l3" class="code_block"><span class="c"># Very simple serial terminal</span>
</div><div id="l4" class="code_block"><span class="c"># (C)2002-2011 Chris Liechti &lt;cliechti@gmx.net&gt;</span>
</div><div id="l5" class="code_block">
</div><div id="l6" class="code_block"><span class="c"># Input characters are sent directly (only LF -&gt; CR/LF/CRLF translation is</span>
</div><div id="l7" class="code_block"><span class="c"># done), received characters are displayed as is (or escaped trough pythons</span>
</div><div id="l8" class="code_block"><span class="c"># repr, useful for debug purposes)</span>
</div><div id="l9" class="code_block">
</div><div id="l10" class="code_block">
</div><div id="l11" class="code_block"><span class="kn">import</span> <span class="nn">sys</span><span class="o">,</span> <span class="nn">os</span><span class="o">,</span> <span class="nn">serial</span><span class="o">,</span> <span class="nn">threading</span>
</div><div id="l12" class="code_block"><span class="k">try</span><span class="p">:</span>
</div><div id="l13" class="code_block">    <span class="kn">from</span> <span class="nn">serial.tools.list_ports</span> <span class="kn">import</span> <span class="n">comports</span>
</div><div id="l14" class="code_block"><span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
</div><div id="l15" class="code_block">    <span class="n">comports</span> <span class="o">=</span> <span class="bp">None</span>
</div><div id="l16" class="code_block">
</div><div id="l17" class="code_block"><span class="n">EXITCHARCTER</span> <span class="o">=</span> <span class="n">serial</span><span class="o">.</span><span class="n">to_bytes</span><span class="p">([</span><span class="mh">0x1d</span><span class="p">])</span>   <span class="c"># GS/CTRL+]</span>
</div><div id="l18" class="code_block"><span class="n">MENUCHARACTER</span> <span class="o">=</span> <span class="n">serial</span><span class="o">.</span><span class="n">to_bytes</span><span class="p">([</span><span class="mh">0x14</span><span class="p">])</span>  <span class="c"># Menu: CTRL+T</span>
</div><div id="l19" class="code_block">
</div><div id="l20" class="code_block"><span class="n">DEFAULT_PORT</span> <span class="o">=</span> <span class="bp">None</span>
</div><div id="l21" class="code_block"><span class="n">DEFAULT_BAUDRATE</span> <span class="o">=</span> <span class="mi">9600</span>
</div><div id="l22" class="code_block"><span class="n">DEFAULT_RTS</span> <span class="o">=</span> <span class="bp">None</span>
</div><div id="l23" class="code_block"><span class="n">DEFAULT_DTR</span> <span class="o">=</span> <span class="bp">None</span>
</div><div id="l24" class="code_block">
</div><div id="l25" class="code_block">
</div><div id="l26" class="code_block"><span class="k">def</span> <span class="nf">key_description</span><span class="p">(</span><span class="n">character</span><span class="p">):</span>
</div><div id="l27" class="code_block">    <span class="sd">&quot;&quot;&quot;generate a readable description for a key&quot;&quot;&quot;</span>
</div><div id="l28" class="code_block">    <span class="n">ascii_code</span> <span class="o">=</span> <span class="nb">ord</span><span class="p">(</span><span class="n">character</span><span class="p">)</span>
</div><div id="l29" class="code_block">    <span class="k">if</span> <span class="n">ascii_code</span> <span class="o">&lt;</span> <span class="mi">32</span><span class="p">:</span>
</div><div id="l30" class="code_block">        <span class="k">return</span> <span class="s">&#39;Ctrl+</span><span class="si">%c</span><span class="s">&#39;</span> <span class="o">%</span> <span class="p">(</span><span class="nb">ord</span><span class="p">(</span><span class="s">&#39;@&#39;</span><span class="p">)</span> <span class="o">+</span> <span class="n">ascii_code</span><span class="p">)</span>
</div><div id="l31" class="code_block">    <span class="k">else</span><span class="p">:</span>
</div><div id="l32" class="code_block">        <span class="k">return</span> <span class="nb">repr</span><span class="p">(</span><span class="n">character</span><span class="p">)</span>
</div><div id="l33" class="code_block">
</div><div id="l34" class="code_block">
</div><div id="l35" class="code_block"><span class="c"># help text, starts with blank line! it&#39;s a function so that the current values</span>
</div><div id="l36" class="code_block"><span class="c"># for the shortcut keys is used and not the value at program start</span>
</div><div id="l37" class="code_block"><span class="k">def</span> <span class="nf">get_help_text</span><span class="p">():</span>
</div><div id="l38" class="code_block">    <span class="k">return</span> <span class="s">&quot;&quot;&quot;</span>
</div><div id="l39" class="code_block"><span class="s">--- pySerial (</span><span class="si">%(version)s</span><span class="s">) - miniterm - help</span>
</div><div id="l40" class="code_block"><span class="s">---</span>
</div><div id="l41" class="code_block"><span class="s">--- </span><span class="si">%(exit)-8s</span><span class="s"> Exit program</span>
</div><div id="l42" class="code_block"><span class="s">--- </span><span class="si">%(menu)-8s</span><span class="s"> Menu escape key, followed by:</span>
</div><div id="l43" class="code_block"><span class="s">--- Menu keys:</span>
</div><div id="l44" class="code_block"><span class="s">---    </span><span class="si">%(itself)-7s</span><span class="s"> Send the menu character itself to remote</span>
</div><div id="l45" class="code_block"><span class="s">---    </span><span class="si">%(exchar)-7s</span><span class="s"> Send the exit character itself to remote</span>
</div><div id="l46" class="code_block"><span class="s">---    </span><span class="si">%(info)-7s</span><span class="s"> Show info</span>
</div><div id="l47" class="code_block"><span class="s">---    </span><span class="si">%(upload)-7s</span><span class="s"> Upload file (prompt will be shown)</span>
</div><div id="l48" class="code_block"><span class="s">--- Toggles:</span>
</div><div id="l49" class="code_block"><span class="s">---    </span><span class="si">%(rts)-7s</span><span class="s"> RTS          </span><span class="si">%(echo)-7s</span><span class="s"> local echo</span>
</div><div id="l50" class="code_block"><span class="s">---    </span><span class="si">%(dtr)-7s</span><span class="s"> DTR          </span><span class="si">%(break)-7s</span><span class="s"> BREAK</span>
</div><div id="l51" class="code_block"><span class="s">---    </span><span class="si">%(lfm)-7s</span><span class="s"> line feed    </span><span class="si">%(repr)-7s</span><span class="s"> Cycle repr mode</span>
</div><div id="l52" class="code_block"><span class="s">---</span>
</div><div id="l53" class="code_block"><span class="s">--- Port settings (</span><span class="si">%(menu)s</span><span class="s"> followed by the following):</span>
</div><div id="l54" class="code_block"><span class="s">---    p          change port</span>
</div><div id="l55" class="code_block"><span class="s">---    7 8        set data bits</span>
</div><div id="l56" class="code_block"><span class="s">---    n e o s m  change parity (None, Even, Odd, Space, Mark)</span>
</div><div id="l57" class="code_block"><span class="s">---    1 2 3      set stop bits (1, 2, 1.5)</span>
</div><div id="l58" class="code_block"><span class="s">---    b          change baud rate</span>
</div><div id="l59" class="code_block"><span class="s">---    x X        disable/enable software flow control</span>
</div><div id="l60" class="code_block"><span class="s">---    r R        disable/enable hardware flow control</span>
</div><div id="l61" class="code_block"><span class="s">&quot;&quot;&quot;</span> <span class="o">%</span> <span class="p">{</span>
</div><div id="l62" class="code_block">    <span class="s">&#39;version&#39;</span><span class="p">:</span> <span class="nb">getattr</span><span class="p">(</span><span class="n">serial</span><span class="p">,</span> <span class="s">&#39;VERSION&#39;</span><span class="p">,</span> <span class="s">&#39;unknown version&#39;</span><span class="p">),</span>
</div><div id="l63" class="code_block">    <span class="s">&#39;exit&#39;</span><span class="p">:</span> <span class="n">key_description</span><span class="p">(</span><span class="n">EXITCHARCTER</span><span class="p">),</span>
</div><div id="l64" class="code_block">    <span class="s">&#39;menu&#39;</span><span class="p">:</span> <span class="n">key_description</span><span class="p">(</span><span class="n">MENUCHARACTER</span><span class="p">),</span>
</div><div id="l65" class="code_block">    <span class="s">&#39;rts&#39;</span><span class="p">:</span> <span class="n">key_description</span><span class="p">(</span><span class="s">&#39;</span><span class="se">\x12</span><span class="s">&#39;</span><span class="p">),</span>
</div><div id="l66" class="code_block">    <span class="s">&#39;repr&#39;</span><span class="p">:</span> <span class="n">key_description</span><span class="p">(</span><span class="s">&#39;</span><span class="se">\x01</span><span class="s">&#39;</span><span class="p">),</span>
</div><div id="l67" class="code_block">    <span class="s">&#39;dtr&#39;</span><span class="p">:</span> <span class="n">key_description</span><span class="p">(</span><span class="s">&#39;</span><span class="se">\x04</span><span class="s">&#39;</span><span class="p">),</span>
</div><div id="l68" class="code_block">    <span class="s">&#39;lfm&#39;</span><span class="p">:</span> <span class="n">key_description</span><span class="p">(</span><span class="s">&#39;</span><span class="se">\x0c</span><span class="s">&#39;</span><span class="p">),</span>
</div><div id="l69" class="code_block">    <span class="s">&#39;break&#39;</span><span class="p">:</span> <span class="n">key_description</span><span class="p">(</span><span class="s">&#39;</span><span class="se">\x02</span><span class="s">&#39;</span><span class="p">),</span>
</div><div id="l70" class="code_block">    <span class="s">&#39;echo&#39;</span><span class="p">:</span> <span class="n">key_description</span><span class="p">(</span><span class="s">&#39;</span><span class="se">\x05</span><span class="s">&#39;</span><span class="p">),</span>
</div><div id="l71" class="code_block">    <span class="s">&#39;info&#39;</span><span class="p">:</span> <span class="n">key_description</span><span class="p">(</span><span class="s">&#39;</span><span class="se">\x09</span><span class="s">&#39;</span><span class="p">),</span>
</div><div id="l72" class="code_block">    <span class="s">&#39;upload&#39;</span><span class="p">:</span> <span class="n">key_description</span><span class="p">(</span><span class="s">&#39;</span><span class="se">\x15</span><span class="s">&#39;</span><span class="p">),</span>
</div><div id="l73" class="code_block">    <span class="s">&#39;itself&#39;</span><span class="p">:</span> <span class="n">key_description</span><span class="p">(</span><span class="n">MENUCHARACTER</span><span class="p">),</span>
</div><div id="l74" class="code_block">    <span class="s">&#39;exchar&#39;</span><span class="p">:</span> <span class="n">key_description</span><span class="p">(</span><span class="n">EXITCHARCTER</span><span class="p">),</span>
</div><div id="l75" class="code_block"><span class="p">}</span>
</div><div id="l76" class="code_block">
</div><div id="l77" class="code_block"><span class="k">if</span> <span class="n">sys</span><span class="o">.</span><span class="n">version_info</span> <span class="o">&gt;=</span> <span class="p">(</span><span class="mi">3</span><span class="p">,</span> <span class="mi">0</span><span class="p">):</span>
</div><div id="l78" class="code_block">    <span class="k">def</span> <span class="nf">character</span><span class="p">(</span><span class="n">b</span><span class="p">):</span>
</div><div id="l79" class="code_block">        <span class="k">return</span> <span class="n">b</span><span class="o">.</span><span class="n">decode</span><span class="p">(</span><span class="s">&#39;latin1&#39;</span><span class="p">)</span>
</div><div id="l80" class="code_block"><span class="k">else</span><span class="p">:</span>
</div><div id="l81" class="code_block">    <span class="k">def</span> <span class="nf">character</span><span class="p">(</span><span class="n">b</span><span class="p">):</span>
</div><div id="l82" class="code_block">        <span class="k">return</span> <span class="n">b</span>
</div><div id="l83" class="code_block">
</div><div id="l84" class="code_block"><span class="n">LF</span> <span class="o">=</span> <span class="n">serial</span><span class="o">.</span><span class="n">to_bytes</span><span class="p">([</span><span class="mi">10</span><span class="p">])</span>
</div><div id="l85" class="code_block"><span class="n">CR</span> <span class="o">=</span> <span class="n">serial</span><span class="o">.</span><span class="n">to_bytes</span><span class="p">([</span><span class="mi">13</span><span class="p">])</span>
</div><div id="l86" class="code_block"><span class="n">CRLF</span> <span class="o">=</span> <span class="n">serial</span><span class="o">.</span><span class="n">to_bytes</span><span class="p">([</span><span class="mi">13</span><span class="p">,</span> <span class="mi">10</span><span class="p">])</span>
</div><div id="l87" class="code_block">
</div><div id="l88" class="code_block"><span class="n">X00</span> <span class="o">=</span> <span class="n">serial</span><span class="o">.</span><span class="n">to_bytes</span><span class="p">([</span><span class="mi">0</span><span class="p">])</span>
</div><div id="l89" class="code_block"><span class="n">X0E</span> <span class="o">=</span> <span class="n">serial</span><span class="o">.</span><span class="n">to_bytes</span><span class="p">([</span><span class="mh">0x0e</span><span class="p">])</span>
</div><div id="l90" class="code_block">
</div><div id="l91" class="code_block"><span class="c"># first choose a platform dependant way to read single characters from the console</span>
</div><div id="l92" class="code_block"><span class="k">global</span> <span class="n">console</span>
</div><div id="l93" class="code_block">
</div><div id="l94" class="code_block"><span class="k">if</span> <span class="n">os</span><span class="o">.</span><span class="n">name</span> <span class="o">==</span> <span class="s">&#39;nt&#39;</span><span class="p">:</span>
</div><div id="l95" class="code_block">    <span class="kn">import</span> <span class="nn">msvcrt</span>
</div><div id="l96" class="code_block">    <span class="k">class</span> <span class="nc">Console</span><span class="p">(</span><span class="nb">object</span><span class="p">):</span>
</div><div id="l97" class="code_block">        <span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</div><div id="l98" class="code_block">            <span class="k">pass</span>
</div><div id="l99" class="code_block">
</div><div id="l100" class="code_block">        <span class="k">def</span> <span class="nf">setup</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</div><div id="l101" class="code_block">            <span class="k">pass</span>    <span class="c"># Do nothing for &#39;nt&#39;</span>
</div><div id="l102" class="code_block">
</div><div id="l103" class="code_block">        <span class="k">def</span> <span class="nf">cleanup</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</div><div id="l104" class="code_block">            <span class="k">pass</span>    <span class="c"># Do nothing for &#39;nt&#39;</span>
</div><div id="l105" class="code_block">
</div><div id="l106" class="code_block">        <span class="k">def</span> <span class="nf">getkey</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</div><div id="l107" class="code_block">            <span class="k">while</span> <span class="bp">True</span><span class="p">:</span>
</div><div id="l108" class="code_block">                <span class="n">z</span> <span class="o">=</span> <span class="n">msvcrt</span><span class="o">.</span><span class="n">getch</span><span class="p">()</span>
</div><div id="l109" class="code_block">                <span class="k">if</span> <span class="n">z</span> <span class="o">==</span> <span class="n">X00</span> <span class="ow">or</span> <span class="n">z</span> <span class="o">==</span> <span class="n">X0E</span><span class="p">:</span>    <span class="c"># functions keys, ignore</span>
</div><div id="l110" class="code_block">                    <span class="n">msvcrt</span><span class="o">.</span><span class="n">getch</span><span class="p">()</span>
</div><div id="l111" class="code_block">                <span class="k">else</span><span class="p">:</span>
</div><div id="l112" class="code_block">                    <span class="k">if</span> <span class="n">z</span> <span class="o">==</span> <span class="n">CR</span><span class="p">:</span>
</div><div id="l113" class="code_block">                        <span class="k">return</span> <span class="n">LF</span>
</div><div id="l114" class="code_block">                    <span class="k">return</span> <span class="n">z</span>
</div><div id="l115" class="code_block">
</div><div id="l116" class="code_block">    <span class="n">console</span> <span class="o">=</span> <span class="n">Console</span><span class="p">()</span>
</div><div id="l117" class="code_block">
</div><div id="l118" class="code_block"><span class="k">elif</span> <span class="n">os</span><span class="o">.</span><span class="n">name</span> <span class="o">==</span> <span class="s">&#39;posix&#39;</span><span class="p">:</span>
</div><div id="l119" class="code_block">    <span class="kn">import</span> <span class="nn">termios</span><span class="o">,</span> <span class="nn">sys</span><span class="o">,</span> <span class="nn">os</span>
</div><div id="l120" class="code_block">    <span class="k">class</span> <span class="nc">Console</span><span class="p">(</span><span class="nb">object</span><span class="p">):</span>
</div><div id="l121" class="code_block">        <span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</div><div id="l122" class="code_block">            <span class="bp">self</span><span class="o">.</span><span class="n">fd</span> <span class="o">=</span> <span class="n">sys</span><span class="o">.</span><span class="n">stdin</span><span class="o">.</span><span class="n">fileno</span><span class="p">()</span>
</div><div id="l123" class="code_block">            <span class="bp">self</span><span class="o">.</span><span class="n">old</span> <span class="o">=</span> <span class="bp">None</span>
</div><div id="l124" class="code_block">
</div><div id="l125" class="code_block">        <span class="k">def</span> <span class="nf">setup</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</div><div id="l126" class="code_block">            <span class="bp">self</span><span class="o">.</span><span class="n">old</span> <span class="o">=</span> <span class="n">termios</span><span class="o">.</span><span class="n">tcgetattr</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">fd</span><span class="p">)</span>
</div><div id="l127" class="code_block">            <span class="n">new</span> <span class="o">=</span> <span class="n">termios</span><span class="o">.</span><span class="n">tcgetattr</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">fd</span><span class="p">)</span>
</div><div id="l128" class="code_block">            <span class="n">new</span><span class="p">[</span><span class="mi">3</span><span class="p">]</span> <span class="o">=</span> <span class="n">new</span><span class="p">[</span><span class="mi">3</span><span class="p">]</span> <span class="o">&amp;</span> <span class="o">~</span><span class="n">termios</span><span class="o">.</span><span class="n">ICANON</span> <span class="o">&amp;</span> <span class="o">~</span><span class="n">termios</span><span class="o">.</span><span class="n">ECHO</span> <span class="o">&amp;</span> <span class="o">~</span><span class="n">termios</span><span class="o">.</span><span class="n">ISIG</span>
</div><div id="l129" class="code_block">            <span class="n">new</span><span class="p">[</span><span class="mi">6</span><span class="p">][</span><span class="n">termios</span><span class="o">.</span><span class="n">VMIN</span><span class="p">]</span> <span class="o">=</span> <span class="mi">1</span>
</div><div id="l130" class="code_block">            <span class="n">new</span><span class="p">[</span><span class="mi">6</span><span class="p">][</span><span class="n">termios</span><span class="o">.</span><span class="n">VTIME</span><span class="p">]</span> <span class="o">=</span> <span class="mi">0</span>
</div><div id="l131" class="code_block">            <span class="n">termios</span><span class="o">.</span><span class="n">tcsetattr</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">fd</span><span class="p">,</span> <span class="n">termios</span><span class="o">.</span><span class="n">TCSANOW</span><span class="p">,</span> <span class="n">new</span><span class="p">)</span>
</div><div id="l132" class="code_block">
</div><div id="l133" class="code_block">        <span class="k">def</span> <span class="nf">getkey</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</div><div id="l134" class="code_block">            <span class="n">c</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">read</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">fd</span><span class="p">,</span> <span class="mi">1</span><span class="p">)</span>
</div><div id="l135" class="code_block">            <span class="k">return</span> <span class="n">c</span>
</div><div id="l136" class="code_block">
</div><div id="l137" class="code_block">        <span class="k">def</span> <span class="nf">cleanup</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</div><div id="l138" class="code_block">            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">old</span> <span class="ow">is</span> <span class="ow">not</span> <span class="bp">None</span><span class="p">:</span>
</div><div id="l139" class="code_block">                <span class="n">termios</span><span class="o">.</span><span class="n">tcsetattr</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">fd</span><span class="p">,</span> <span class="n">termios</span><span class="o">.</span><span class="n">TCSAFLUSH</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">old</span><span class="p">)</span>
</div><div id="l140" class="code_block">
</div><div id="l141" class="code_block">    <span class="n">console</span> <span class="o">=</span> <span class="n">Console</span><span class="p">()</span>
</div><div id="l142" class="code_block">
</div><div id="l143" class="code_block">    <span class="k">def</span> <span class="nf">cleanup_console</span><span class="p">():</span>
</div><div id="l144" class="code_block">        <span class="n">console</span><span class="o">.</span><span class="n">cleanup</span><span class="p">()</span>
</div><div id="l145" class="code_block">
</div><div id="l146" class="code_block">    <span class="n">sys</span><span class="o">.</span><span class="n">exitfunc</span> <span class="o">=</span> <span class="n">cleanup_console</span>      <span class="c"># terminal modes have to be restored on exit...</span>
</div><div id="l147" class="code_block">
</div><div id="l148" class="code_block"><span class="k">else</span><span class="p">:</span>
</div><div id="l149" class="code_block">    <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">(</span><span class="s">&quot;Sorry no implementation for your platform (</span><span class="si">%s</span><span class="s">) available.&quot;</span> <span class="o">%</span> <span class="n">sys</span><span class="o">.</span><span class="n">platform</span><span class="p">)</span>
</div><div id="l150" class="code_block">
</div><div id="l151" class="code_block">
</div><div id="l152" class="code_block"><span class="k">def</span> <span class="nf">dump_port_list</span><span class="p">():</span>
</div><div id="l153" class="code_block">    <span class="k">if</span> <span class="n">comports</span><span class="p">:</span>
</div><div id="l154" class="code_block">        <span class="n">sys</span><span class="o">.</span><span class="n">stderr</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="s">&#39;</span><span class="se">\n</span><span class="s">--- Available ports:</span><span class="se">\n</span><span class="s">&#39;</span><span class="p">)</span>
</div><div id="l155" class="code_block">        <span class="k">for</span> <span class="n">port</span><span class="p">,</span> <span class="n">desc</span><span class="p">,</span> <span class="n">hwid</span> <span class="ow">in</span> <span class="nb">sorted</span><span class="p">(</span><span class="n">comports</span><span class="p">()):</span>
</div><div id="l156" class="code_block">            <span class="c">#~ sys.stderr.write(&#39;--- %-20s %s [%s]\n&#39; % (port, desc, hwid))</span>
</div><div id="l157" class="code_block">            <span class="n">sys</span><span class="o">.</span><span class="n">stderr</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="s">&#39;--- </span><span class="si">%-20s</span><span class="s"> </span><span class="si">%s</span><span class="se">\n</span><span class="s">&#39;</span> <span class="o">%</span> <span class="p">(</span><span class="n">port</span><span class="p">,</span> <span class="n">desc</span><span class="p">))</span>
</div><div id="l158" class="code_block">
</div><div id="l159" class="code_block">
</div><div id="l160" class="code_block"><span class="n">CONVERT_CRLF</span> <span class="o">=</span> <span class="mi">2</span>
</div><div id="l161" class="code_block"><span class="n">CONVERT_CR</span>   <span class="o">=</span> <span class="mi">1</span>
</div><div id="l162" class="code_block"><span class="n">CONVERT_LF</span>   <span class="o">=</span> <span class="mi">0</span>
</div><div id="l163" class="code_block"><span class="n">NEWLINE_CONVERISON_MAP</span> <span class="o">=</span> <span class="p">(</span><span class="n">LF</span><span class="p">,</span> <span class="n">CR</span><span class="p">,</span> <span class="n">CRLF</span><span class="p">)</span>
</div><div id="l164" class="code_block"><span class="n">LF_MODES</span> <span class="o">=</span> <span class="p">(</span><span class="s">&#39;LF&#39;</span><span class="p">,</span> <span class="s">&#39;CR&#39;</span><span class="p">,</span> <span class="s">&#39;CR/LF&#39;</span><span class="p">)</span>
</div><div id="l165" class="code_block">
</div><div id="l166" class="code_block"><span class="n">REPR_MODES</span> <span class="o">=</span> <span class="p">(</span><span class="s">&#39;raw&#39;</span><span class="p">,</span> <span class="s">&#39;some control&#39;</span><span class="p">,</span> <span class="s">&#39;all control&#39;</span><span class="p">,</span> <span class="s">&#39;hex&#39;</span><span class="p">)</span>
</div><div id="l167" class="code_block">
</div><div id="l168" class="code_block"><span class="k">class</span> <span class="nc">Miniterm</span><span class="p">(</span><span class="nb">object</span><span class="p">):</span>
</div><div id="l169" class="code_block">    <span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">port</span><span class="p">,</span> <span class="n">baudrate</span><span class="p">,</span> <span class="n">parity</span><span class="p">,</span> <span class="n">rtscts</span><span class="p">,</span> <span class="n">xonxoff</span><span class="p">,</span> <span class="n">echo</span><span class="o">=</span><span class="bp">False</span><span class="p">,</span> <span class="n">convert_outgoing</span><span class="o">=</span><span class="n">CONVERT_CRLF</span><span class="p">,</span> <span class="n">repr_mode</span><span class="o">=</span><span class="mi">0</span><span class="p">):</span>
</div><div id="l170" class="code_block">        <span class="k">try</span><span class="p">:</span>
</div><div id="l171" class="code_block">            <span class="bp">self</span><span class="o">.</span><span class="n">serial</span> <span class="o">=</span> <span class="n">serial</span><span class="o">.</span><span class="n">serial_for_url</span><span class="p">(</span><span class="n">port</span><span class="p">,</span> <span class="n">baudrate</span><span class="p">,</span> <span class="n">parity</span><span class="o">=</span><span class="n">parity</span><span class="p">,</span> <span class="n">rtscts</span><span class="o">=</span><span class="n">rtscts</span><span class="p">,</span> <span class="n">xonxoff</span><span class="o">=</span><span class="n">xonxoff</span><span class="p">,</span> <span class="n">timeout</span><span class="o">=</span><span class="mi">1</span><span class="p">)</span>
</div><div id="l172" class="code_block">        <span class="k">except</span> <span class="ne">AttributeError</span><span class="p">:</span>
</div><div id="l173" class="code_block">            <span class="c"># happens when the installed pyserial is older than 2.5. use the</span>
</div><div id="l174" class="code_block">            <span class="c"># Serial class directly then.</span>
</div><div id="l175" class="code_block">            <span class="bp">self</span><span class="o">.</span><span class="n">serial</span> <span class="o">=</span> <span class="n">serial</span><span class="o">.</span><span class="n">Serial</span><span class="p">(</span><span class="n">port</span><span class="p">,</span> <span class="n">baudrate</span><span class="p">,</span> <span class="n">parity</span><span class="o">=</span><span class="n">parity</span><span class="p">,</span> <span class="n">rtscts</span><span class="o">=</span><span class="n">rtscts</span><span class="p">,</span> <span class="n">xonxoff</span><span class="o">=</span><span class="n">xonxoff</span><span class="p">,</span> <span class="n">timeout</span><span class="o">=</span><span class="mi">1</span><span class="p">)</span>
</div><div id="l176" class="code_block">        <span class="bp">self</span><span class="o">.</span><span class="n">echo</span> <span class="o">=</span> <span class="n">echo</span>
</div><div id="l177" class="code_block">        <span class="bp">self</span><span class="o">.</span><span class="n">repr_mode</span> <span class="o">=</span> <span class="n">repr_mode</span>
</div><div id="l178" class="code_block">        <span class="bp">self</span><span class="o">.</span><span class="n">convert_outgoing</span> <span class="o">=</span> <span class="n">convert_outgoing</span>
</div><div id="l179" class="code_block">        <span class="bp">self</span><span class="o">.</span><span class="n">newline</span> <span class="o">=</span> <span class="n">NEWLINE_CONVERISON_MAP</span><span class="p">[</span><span class="bp">self</span><span class="o">.</span><span class="n">convert_outgoing</span><span class="p">]</span>
</div><div id="l180" class="code_block">        <span class="bp">self</span><span class="o">.</span><span class="n">dtr_state</span> <span class="o">=</span> <span class="bp">True</span>
</div><div id="l181" class="code_block">        <span class="bp">self</span><span class="o">.</span><span class="n">rts_state</span> <span class="o">=</span> <span class="bp">True</span>
</div><div id="l182" class="code_block">        <span class="bp">self</span><span class="o">.</span><span class="n">break_state</span> <span class="o">=</span> <span class="bp">False</span>
</div><div id="l183" class="code_block">
</div><div id="l184" class="code_block">    <span class="k">def</span> <span class="nf">_start_reader</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</div><div id="l185" class="code_block">        <span class="sd">&quot;&quot;&quot;Start reader thread&quot;&quot;&quot;</span>
</div><div id="l186" class="code_block">        <span class="bp">self</span><span class="o">.</span><span class="n">_reader_alive</span> <span class="o">=</span> <span class="bp">True</span>
</div><div id="l187" class="code_block">        <span class="c"># start serial-&gt;console thread</span>
</div><div id="l188" class="code_block">        <span class="bp">self</span><span class="o">.</span><span class="n">receiver_thread</span> <span class="o">=</span> <span class="n">threading</span><span class="o">.</span><span class="n">Thread</span><span class="p">(</span><span class="n">target</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">reader</span><span class="p">)</span>
</div><div id="l189" class="code_block">        <span class="bp">self</span><span class="o">.</span><span class="n">receiver_thread</span><span class="o">.</span><span class="n">setDaemon</span><span class="p">(</span><span class="bp">True</span><span class="p">)</span>
</div><div id="l190" class="code_block">        <span class="bp">self</span><span class="o">.</span><span class="n">receiver_thread</span><span class="o">.</span><span class="n">start</span><span class="p">()</span>
</div><div id="l191" class="code_block">
</div><div id="l192" class="code_block">    <span class="k">def</span> <span class="nf">_stop_reader</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</div><div id="l193" class="code_block">        <span class="sd">&quot;&quot;&quot;Stop reader thread only, wait for clean exit of thread&quot;&quot;&quot;</span>
</div><div id="l194" class="code_block">        <span class="bp">self</span><span class="o">.</span><span class="n">_reader_alive</span> <span class="o">=</span> <span class="bp">False</span>
</div><div id="l195" class="code_block">        <span class="bp">self</span><span class="o">.</span><span class="n">receiver_thread</span><span class="o">.</span><span class="n">join</span><span class="p">()</span>
</div><div id="l196" class="code_block">
</div><div id="l197" class="code_block">
</div><div id="l198" class="code_block">    <span class="k">def</span> <span class="nf">start</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</div><div id="l199" class="code_block">        <span class="bp">self</span><span class="o">.</span><span class="n">alive</span> <span class="o">=</span> <span class="bp">True</span>
</div><div id="l200" class="code_block">        <span class="bp">self</span><span class="o">.</span><span class="n">_start_reader</span><span class="p">()</span>
</div><div id="l201" class="code_block">        <span class="c"># enter console-&gt;serial loop</span>
</div><div id="l202" class="code_block">        <span class="bp">self</span><span class="o">.</span><span class="n">transmitter_thread</span> <span class="o">=</span> <span class="n">threading</span><span class="o">.</span><span class="n">Thread</span><span class="p">(</span><span class="n">target</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">writer</span><span class="p">)</span>
</div><div id="l203" class="code_block">        <span class="bp">self</span><span class="o">.</span><span class="n">transmitter_thread</span><span class="o">.</span><span class="n">setDaemon</span><span class="p">(</span><span class="bp">True</span><span class="p">)</span>
</div><div id="l204" class="code_block">        <span class="bp">self</span><span class="o">.</span><span class="n">transmitter_thread</span><span class="o">.</span><span class="n">start</span><span class="p">()</span>
</div><div id="l205" class="code_block">
</div><div id="l206" class="code_block">    <span class="k">def</span> <span class="nf">stop</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</div><div id="l207" class="code_block">        <span class="bp">self</span><span class="o">.</span><span class="n">alive</span> <span class="o">=</span> <span class="bp">False</span>
</div><div id="l208" class="code_block">
</div><div id="l209" class="code_block">    <span class="k">def</span> <span class="nf">join</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">transmit_only</span><span class="o">=</span><span class="bp">False</span><span class="p">):</span>
</div><div id="l210" class="code_block">        <span class="bp">self</span><span class="o">.</span><span class="n">transmitter_thread</span><span class="o">.</span><span class="n">join</span><span class="p">()</span>
</div><div id="l211" class="code_block">        <span class="k">if</span> <span class="ow">not</span> <span class="n">transmit_only</span><span class="p">:</span>
</div><div id="l212" class="code_block">            <span class="bp">self</span><span class="o">.</span><span class="n">receiver_thread</span><span class="o">.</span><span class="n">join</span><span class="p">()</span>
</div><div id="l213" class="code_block">
</div><div id="l214" class="code_block">    <span class="k">def</span> <span class="nf">dump_port_settings</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</div><div id="l215" class="code_block">        <span class="n">sys</span><span class="o">.</span><span class="n">stderr</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="s">&quot;</span><span class="se">\n</span><span class="s">--- Settings: </span><span class="si">%s</span><span class="s">  </span><span class="si">%s</span><span class="s">,</span><span class="si">%s</span><span class="s">,</span><span class="si">%s</span><span class="s">,</span><span class="si">%s</span><span class="se">\n</span><span class="s">&quot;</span> <span class="o">%</span> <span class="p">(</span>
</div><div id="l216" class="code_block">                <span class="bp">self</span><span class="o">.</span><span class="n">serial</span><span class="o">.</span><span class="n">portstr</span><span class="p">,</span>
</div><div id="l217" class="code_block">                <span class="bp">self</span><span class="o">.</span><span class="n">serial</span><span class="o">.</span><span class="n">baudrate</span><span class="p">,</span>
</div><div id="l218" class="code_block">                <span class="bp">self</span><span class="o">.</span><span class="n">serial</span><span class="o">.</span><span class="n">bytesize</span><span class="p">,</span>
</div><div id="l219" class="code_block">                <span class="bp">self</span><span class="o">.</span><span class="n">serial</span><span class="o">.</span><span class="n">parity</span><span class="p">,</span>
</div><div id="l220" class="code_block">                <span class="bp">self</span><span class="o">.</span><span class="n">serial</span><span class="o">.</span><span class="n">stopbits</span><span class="p">))</span>
</div><div id="l221" class="code_block">        <span class="n">sys</span><span class="o">.</span><span class="n">stderr</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="s">&#39;--- RTS: </span><span class="si">%-8s</span><span class="s">  DTR: </span><span class="si">%-8s</span><span class="s">  BREAK: </span><span class="si">%-8s</span><span class="se">\n</span><span class="s">&#39;</span> <span class="o">%</span> <span class="p">(</span>
</div><div id="l222" class="code_block">                <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">rts_state</span> <span class="ow">and</span> <span class="s">&#39;active&#39;</span> <span class="ow">or</span> <span class="s">&#39;inactive&#39;</span><span class="p">),</span>
</div><div id="l223" class="code_block">                <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">dtr_state</span> <span class="ow">and</span> <span class="s">&#39;active&#39;</span> <span class="ow">or</span> <span class="s">&#39;inactive&#39;</span><span class="p">),</span>
</div><div id="l224" class="code_block">                <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">break_state</span> <span class="ow">and</span> <span class="s">&#39;active&#39;</span> <span class="ow">or</span> <span class="s">&#39;inactive&#39;</span><span class="p">)))</span>
</div><div id="l225" class="code_block">        <span class="k">try</span><span class="p">:</span>
</div><div id="l226" class="code_block">            <span class="n">sys</span><span class="o">.</span><span class="n">stderr</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="s">&#39;--- CTS: </span><span class="si">%-8s</span><span class="s">  DSR: </span><span class="si">%-8s</span><span class="s">  RI: </span><span class="si">%-8s</span><span class="s">  CD: </span><span class="si">%-8s</span><span class="se">\n</span><span class="s">&#39;</span> <span class="o">%</span> <span class="p">(</span>
</div><div id="l227" class="code_block">                    <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">serial</span><span class="o">.</span><span class="n">getCTS</span><span class="p">()</span> <span class="ow">and</span> <span class="s">&#39;active&#39;</span> <span class="ow">or</span> <span class="s">&#39;inactive&#39;</span><span class="p">),</span>
</div><div id="l228" class="code_block">                    <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">serial</span><span class="o">.</span><span class="n">getDSR</span><span class="p">()</span> <span class="ow">and</span> <span class="s">&#39;active&#39;</span> <span class="ow">or</span> <span class="s">&#39;inactive&#39;</span><span class="p">),</span>
</div><div id="l229" class="code_block">                    <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">serial</span><span class="o">.</span><span class="n">getRI</span><span class="p">()</span> <span class="ow">and</span> <span class="s">&#39;active&#39;</span> <span class="ow">or</span> <span class="s">&#39;inactive&#39;</span><span class="p">),</span>
</div><div id="l230" class="code_block">                    <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">serial</span><span class="o">.</span><span class="n">getCD</span><span class="p">()</span> <span class="ow">and</span> <span class="s">&#39;active&#39;</span> <span class="ow">or</span> <span class="s">&#39;inactive&#39;</span><span class="p">)))</span>
</div><div id="l231" class="code_block">        <span class="k">except</span> <span class="n">serial</span><span class="o">.</span><span class="n">SerialException</span><span class="p">:</span>
</div><div id="l232" class="code_block">            <span class="c"># on RFC 2217 ports it can happen to no modem state notification was</span>
</div><div id="l233" class="code_block">            <span class="c"># yet received. ignore this error.</span>
</div><div id="l234" class="code_block">            <span class="k">pass</span>
</div><div id="l235" class="code_block">        <span class="n">sys</span><span class="o">.</span><span class="n">stderr</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="s">&#39;--- software flow control: </span><span class="si">%s</span><span class="se">\n</span><span class="s">&#39;</span> <span class="o">%</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">serial</span><span class="o">.</span><span class="n">xonxoff</span> <span class="ow">and</span> <span class="s">&#39;active&#39;</span> <span class="ow">or</span> <span class="s">&#39;inactive&#39;</span><span class="p">))</span>
</div><div id="l236" class="code_block">        <span class="n">sys</span><span class="o">.</span><span class="n">stderr</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="s">&#39;--- hardware flow control: </span><span class="si">%s</span><span class="se">\n</span><span class="s">&#39;</span> <span class="o">%</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">serial</span><span class="o">.</span><span class="n">rtscts</span> <span class="ow">and</span> <span class="s">&#39;active&#39;</span> <span class="ow">or</span> <span class="s">&#39;inactive&#39;</span><span class="p">))</span>
</div><div id="l237" class="code_block">        <span class="n">sys</span><span class="o">.</span><span class="n">stderr</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="s">&#39;--- data escaping: </span><span class="si">%s</span><span class="s">  linefeed: </span><span class="si">%s</span><span class="se">\n</span><span class="s">&#39;</span> <span class="o">%</span> <span class="p">(</span>
</div><div id="l238" class="code_block">                <span class="n">REPR_MODES</span><span class="p">[</span><span class="bp">self</span><span class="o">.</span><span class="n">repr_mode</span><span class="p">],</span>
</div><div id="l239" class="code_block">                <span class="n">LF_MODES</span><span class="p">[</span><span class="bp">self</span><span class="o">.</span><span class="n">convert_outgoing</span><span class="p">]))</span>
</div><div id="l240" class="code_block">
</div><div id="l241" class="code_block">    <span class="k">def</span> <span class="nf">reader</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</div><div id="l242" class="code_block">        <span class="sd">&quot;&quot;&quot;loop and copy serial-&gt;console&quot;&quot;&quot;</span>
</div><div id="l243" class="code_block">        <span class="k">try</span><span class="p">:</span>
</div><div id="l244" class="code_block">            <span class="k">while</span> <span class="bp">self</span><span class="o">.</span><span class="n">alive</span> <span class="ow">and</span> <span class="bp">self</span><span class="o">.</span><span class="n">_reader_alive</span><span class="p">:</span>
</div><div id="l245" class="code_block">                <span class="n">data</span> <span class="o">=</span> <span class="n">character</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">serial</span><span class="o">.</span><span class="n">read</span><span class="p">(</span><span class="mi">1</span><span class="p">))</span>
</div><div id="l246" class="code_block">
</div><div id="l247" class="code_block">                <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">repr_mode</span> <span class="o">==</span> <span class="mi">0</span><span class="p">:</span>
</div><div id="l248" class="code_block">                    <span class="c"># direct output, just have to care about newline setting</span>
</div><div id="l249" class="code_block">                    <span class="k">if</span> <span class="n">data</span> <span class="o">==</span> <span class="s">&#39;</span><span class="se">\r</span><span class="s">&#39;</span> <span class="ow">and</span> <span class="bp">self</span><span class="o">.</span><span class="n">convert_outgoing</span> <span class="o">==</span> <span class="n">CONVERT_CR</span><span class="p">:</span>
</div><div id="l250" class="code_block">                        <span class="n">sys</span><span class="o">.</span><span class="n">stdout</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="s">&#39;</span><span class="se">\n</span><span class="s">&#39;</span><span class="p">)</span>
</div><div id="l251" class="code_block">                    <span class="k">else</span><span class="p">:</span>
</div><div id="l252" class="code_block">                        <span class="n">sys</span><span class="o">.</span><span class="n">stdout</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="n">data</span><span class="p">)</span>
</div><div id="l253" class="code_block">                <span class="k">elif</span> <span class="bp">self</span><span class="o">.</span><span class="n">repr_mode</span> <span class="o">==</span> <span class="mi">1</span><span class="p">:</span>
</div><div id="l254" class="code_block">                    <span class="c"># escape non-printable, let pass newlines</span>
</div><div id="l255" class="code_block">                    <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">convert_outgoing</span> <span class="o">==</span> <span class="n">CONVERT_CRLF</span> <span class="ow">and</span> <span class="n">data</span> <span class="ow">in</span> <span class="s">&#39;</span><span class="se">\r\n</span><span class="s">&#39;</span><span class="p">:</span>
</div><div id="l256" class="code_block">                        <span class="k">if</span> <span class="n">data</span> <span class="o">==</span> <span class="s">&#39;</span><span class="se">\n</span><span class="s">&#39;</span><span class="p">:</span>
</div><div id="l257" class="code_block">                            <span class="n">sys</span><span class="o">.</span><span class="n">stdout</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="s">&#39;</span><span class="se">\n</span><span class="s">&#39;</span><span class="p">)</span>
</div><div id="l258" class="code_block">                        <span class="k">elif</span> <span class="n">data</span> <span class="o">==</span> <span class="s">&#39;</span><span class="se">\r</span><span class="s">&#39;</span><span class="p">:</span>
</div><div id="l259" class="code_block">                            <span class="k">pass</span>
</div><div id="l260" class="code_block">                    <span class="k">elif</span> <span class="n">data</span> <span class="o">==</span> <span class="s">&#39;</span><span class="se">\n</span><span class="s">&#39;</span> <span class="ow">and</span> <span class="bp">self</span><span class="o">.</span><span class="n">convert_outgoing</span> <span class="o">==</span> <span class="n">CONVERT_LF</span><span class="p">:</span>
</div><div id="l261" class="code_block">                        <span class="n">sys</span><span class="o">.</span><span class="n">stdout</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="s">&#39;</span><span class="se">\n</span><span class="s">&#39;</span><span class="p">)</span>
</div><div id="l262" class="code_block">                    <span class="k">elif</span> <span class="n">data</span> <span class="o">==</span> <span class="s">&#39;</span><span class="se">\r</span><span class="s">&#39;</span> <span class="ow">and</span> <span class="bp">self</span><span class="o">.</span><span class="n">convert_outgoing</span> <span class="o">==</span> <span class="n">CONVERT_CR</span><span class="p">:</span>
</div><div id="l263" class="code_block">                        <span class="n">sys</span><span class="o">.</span><span class="n">stdout</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="s">&#39;</span><span class="se">\n</span><span class="s">&#39;</span><span class="p">)</span>
</div><div id="l264" class="code_block">                    <span class="k">else</span><span class="p">:</span>
</div><div id="l265" class="code_block">                        <span class="n">sys</span><span class="o">.</span><span class="n">stdout</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="nb">repr</span><span class="p">(</span><span class="n">data</span><span class="p">)[</span><span class="mi">1</span><span class="p">:</span><span class="o">-</span><span class="mi">1</span><span class="p">])</span>
</div><div id="l266" class="code_block">                <span class="k">elif</span> <span class="bp">self</span><span class="o">.</span><span class="n">repr_mode</span> <span class="o">==</span> <span class="mi">2</span><span class="p">:</span>
</div><div id="l267" class="code_block">                    <span class="c"># escape all non-printable, including newline</span>
</div><div id="l268" class="code_block">                    <span class="n">sys</span><span class="o">.</span><span class="n">stdout</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="nb">repr</span><span class="p">(</span><span class="n">data</span><span class="p">)[</span><span class="mi">1</span><span class="p">:</span><span class="o">-</span><span class="mi">1</span><span class="p">])</span>
</div><div id="l269" class="code_block">                <span class="k">elif</span> <span class="bp">self</span><span class="o">.</span><span class="n">repr_mode</span> <span class="o">==</span> <span class="mi">3</span><span class="p">:</span>
</div><div id="l270" class="code_block">                    <span class="c"># escape everything (hexdump)</span>
</div><div id="l271" class="code_block">                    <span class="k">for</span> <span class="n">c</span> <span class="ow">in</span> <span class="n">data</span><span class="p">:</span>
</div><div id="l272" class="code_block">                        <span class="n">sys</span><span class="o">.</span><span class="n">stdout</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="s">&quot;</span><span class="si">%s</span><span class="s"> &quot;</span> <span class="o">%</span> <span class="n">c</span><span class="o">.</span><span class="n">encode</span><span class="p">(</span><span class="s">&#39;hex&#39;</span><span class="p">))</span>
</div><div id="l273" class="code_block">                <span class="n">sys</span><span class="o">.</span><span class="n">stdout</span><span class="o">.</span><span class="n">flush</span><span class="p">()</span>
</div><div id="l274" class="code_block">        <span class="k">except</span> <span class="n">serial</span><span class="o">.</span><span class="n">SerialException</span><span class="p">,</span> <span class="n">e</span><span class="p">:</span>
</div><div id="l275" class="code_block">            <span class="bp">self</span><span class="o">.</span><span class="n">alive</span> <span class="o">=</span> <span class="bp">False</span>
</div><div id="l276" class="code_block">            <span class="c"># would be nice if the console reader could be interruptted at this</span>
</div><div id="l277" class="code_block">            <span class="c"># point...</span>
</div><div id="l278" class="code_block">            <span class="k">raise</span>
</div><div id="l279" class="code_block">
</div><div id="l280" class="code_block">
</div><div id="l281" class="code_block">    <span class="k">def</span> <span class="nf">writer</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</div><div id="l282" class="code_block">        <span class="sd">&quot;&quot;&quot;\</span>
</div><div id="l283" class="code_block"><span class="sd">        Loop and copy console-&gt;serial until EXITCHARCTER character is</span>
</div><div id="l284" class="code_block"><span class="sd">        found. When MENUCHARACTER is found, interpret the next key</span>
</div><div id="l285" class="code_block"><span class="sd">        locally.</span>
</div><div id="l286" class="code_block"><span class="sd">        &quot;&quot;&quot;</span>
</div><div id="l287" class="code_block">        <span class="n">menu_active</span> <span class="o">=</span> <span class="bp">False</span>
</div><div id="l288" class="code_block">        <span class="k">try</span><span class="p">:</span>
</div><div id="l289" class="code_block">            <span class="k">while</span> <span class="bp">self</span><span class="o">.</span><span class="n">alive</span><span class="p">:</span>
</div><div id="l290" class="code_block">                <span class="k">try</span><span class="p">:</span>
</div><div id="l291" class="code_block">                    <span class="n">b</span> <span class="o">=</span> <span class="n">console</span><span class="o">.</span><span class="n">getkey</span><span class="p">()</span>
</div><div id="l292" class="code_block">                <span class="k">except</span> <span class="ne">KeyboardInterrupt</span><span class="p">:</span>
</div><div id="l293" class="code_block">                    <span class="n">b</span> <span class="o">=</span> <span class="n">serial</span><span class="o">.</span><span class="n">to_bytes</span><span class="p">([</span><span class="mi">3</span><span class="p">])</span>
</div><div id="l294" class="code_block">                <span class="n">c</span> <span class="o">=</span> <span class="n">character</span><span class="p">(</span><span class="n">b</span><span class="p">)</span>
</div><div id="l295" class="code_block">                <span class="k">if</span> <span class="n">menu_active</span><span class="p">:</span>
</div><div id="l296" class="code_block">                    <span class="k">if</span> <span class="n">c</span> <span class="o">==</span> <span class="n">MENUCHARACTER</span> <span class="ow">or</span> <span class="n">c</span> <span class="o">==</span> <span class="n">EXITCHARCTER</span><span class="p">:</span> <span class="c"># Menu character again/exit char -&gt; send itself</span>
</div><div id="l297" class="code_block">                        <span class="bp">self</span><span class="o">.</span><span class="n">serial</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="n">b</span><span class="p">)</span>                    <span class="c"># send character</span>
</div><div id="l298" class="code_block">                        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">echo</span><span class="p">:</span>
</div><div id="l299" class="code_block">                            <span class="n">sys</span><span class="o">.</span><span class="n">stdout</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="n">c</span><span class="p">)</span>
</div><div id="l300" class="code_block">                    <span class="k">elif</span> <span class="n">c</span> <span class="o">==</span> <span class="s">&#39;</span><span class="se">\x15</span><span class="s">&#39;</span><span class="p">:</span>                       <span class="c"># CTRL+U -&gt; upload file</span>
</div><div id="l301" class="code_block">                        <span class="n">sys</span><span class="o">.</span><span class="n">stderr</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="s">&#39;</span><span class="se">\n</span><span class="s">--- File to upload: &#39;</span><span class="p">)</span>
</div><div id="l302" class="code_block">                        <span class="n">sys</span><span class="o">.</span><span class="n">stderr</span><span class="o">.</span><span class="n">flush</span><span class="p">()</span>
</div><div id="l303" class="code_block">                        <span class="n">console</span><span class="o">.</span><span class="n">cleanup</span><span class="p">()</span>
</div><div id="l304" class="code_block">                        <span class="n">filename</span> <span class="o">=</span> <span class="n">sys</span><span class="o">.</span><span class="n">stdin</span><span class="o">.</span><span class="n">readline</span><span class="p">()</span><span class="o">.</span><span class="n">rstrip</span><span class="p">(</span><span class="s">&#39;</span><span class="se">\r\n</span><span class="s">&#39;</span><span class="p">)</span>
</div><div id="l305" class="code_block">                        <span class="k">if</span> <span class="n">filename</span><span class="p">:</span>
</div><div id="l306" class="code_block">                            <span class="k">try</span><span class="p">:</span>
</div><div id="l307" class="code_block">                                <span class="nb">file</span> <span class="o">=</span> <span class="nb">open</span><span class="p">(</span><span class="n">filename</span><span class="p">,</span> <span class="s">&#39;r&#39;</span><span class="p">)</span>
</div><div id="l308" class="code_block">                                <span class="n">sys</span><span class="o">.</span><span class="n">stderr</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="s">&#39;--- Sending file </span><span class="si">%s</span><span class="s"> ---</span><span class="se">\n</span><span class="s">&#39;</span> <span class="o">%</span> <span class="n">filename</span><span class="p">)</span>
</div><div id="l309" class="code_block">                                <span class="k">while</span> <span class="bp">True</span><span class="p">:</span>
</div><div id="l310" class="code_block">                                    <span class="n">line</span> <span class="o">=</span> <span class="nb">file</span><span class="o">.</span><span class="n">readline</span><span class="p">()</span><span class="o">.</span><span class="n">rstrip</span><span class="p">(</span><span class="s">&#39;</span><span class="se">\r\n</span><span class="s">&#39;</span><span class="p">)</span>
</div><div id="l311" class="code_block">                                    <span class="k">if</span> <span class="ow">not</span> <span class="n">line</span><span class="p">:</span>
</div><div id="l312" class="code_block">                                        <span class="k">break</span>
</div><div id="l313" class="code_block">                                    <span class="bp">self</span><span class="o">.</span><span class="n">serial</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="n">line</span><span class="p">)</span>
</div><div id="l314" class="code_block">                                    <span class="bp">self</span><span class="o">.</span><span class="n">serial</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="s">&#39;</span><span class="se">\r\n</span><span class="s">&#39;</span><span class="p">)</span>
</div><div id="l315" class="code_block">                                    <span class="c"># Wait for output buffer to drain.</span>
</div><div id="l316" class="code_block">                                    <span class="bp">self</span><span class="o">.</span><span class="n">serial</span><span class="o">.</span><span class="n">flush</span><span class="p">()</span>
</div><div id="l317" class="code_block">                                    <span class="n">sys</span><span class="o">.</span><span class="n">stderr</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="s">&#39;.&#39;</span><span class="p">)</span>   <span class="c"># Progress indicator.</span>
</div><div id="l318" class="code_block">                                <span class="n">sys</span><span class="o">.</span><span class="n">stderr</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="s">&#39;</span><span class="se">\n</span><span class="s">--- File </span><span class="si">%s</span><span class="s"> sent ---</span><span class="se">\n</span><span class="s">&#39;</span> <span class="o">%</span> <span class="n">filename</span><span class="p">)</span>
</div><div id="l319" class="code_block">                            <span class="k">except</span> <span class="ne">IOError</span><span class="p">,</span> <span class="n">e</span><span class="p">:</span>
</div><div id="l320" class="code_block">                                <span class="n">sys</span><span class="o">.</span><span class="n">stderr</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="s">&#39;--- ERROR opening file </span><span class="si">%s</span><span class="s">: </span><span class="si">%s</span><span class="s"> ---</span><span class="se">\n</span><span class="s">&#39;</span> <span class="o">%</span> <span class="p">(</span><span class="n">filename</span><span class="p">,</span> <span class="n">e</span><span class="p">))</span>
</div><div id="l321" class="code_block">                        <span class="n">console</span><span class="o">.</span><span class="n">setup</span><span class="p">()</span>
</div><div id="l322" class="code_block">                    <span class="k">elif</span> <span class="n">c</span> <span class="ow">in</span> <span class="s">&#39;</span><span class="se">\x08</span><span class="s">hH?&#39;</span><span class="p">:</span>                    <span class="c"># CTRL+H, h, H, ? -&gt; Show help</span>
</div><div id="l323" class="code_block">                        <span class="n">sys</span><span class="o">.</span><span class="n">stderr</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="n">get_help_text</span><span class="p">())</span>
</div><div id="l324" class="code_block">                    <span class="k">elif</span> <span class="n">c</span> <span class="o">==</span> <span class="s">&#39;</span><span class="se">\x12</span><span class="s">&#39;</span><span class="p">:</span>                       <span class="c"># CTRL+R -&gt; Toggle RTS</span>
</div><div id="l325" class="code_block">                        <span class="bp">self</span><span class="o">.</span><span class="n">rts_state</span> <span class="o">=</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">rts_state</span>
</div><div id="l326" class="code_block">                        <span class="bp">self</span><span class="o">.</span><span class="n">serial</span><span class="o">.</span><span class="n">setRTS</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">rts_state</span><span class="p">)</span>
</div><div id="l327" class="code_block">                        <span class="n">sys</span><span class="o">.</span><span class="n">stderr</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="s">&#39;--- RTS </span><span class="si">%s</span><span class="s"> ---</span><span class="se">\n</span><span class="s">&#39;</span> <span class="o">%</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">rts_state</span> <span class="ow">and</span> <span class="s">&#39;active&#39;</span> <span class="ow">or</span> <span class="s">&#39;inactive&#39;</span><span class="p">))</span>
</div><div id="l328" class="code_block">                    <span class="k">elif</span> <span class="n">c</span> <span class="o">==</span> <span class="s">&#39;</span><span class="se">\x04</span><span class="s">&#39;</span><span class="p">:</span>                       <span class="c"># CTRL+D -&gt; Toggle DTR</span>
</div><div id="l329" class="code_block">                        <span class="bp">self</span><span class="o">.</span><span class="n">dtr_state</span> <span class="o">=</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">dtr_state</span>
</div><div id="l330" class="code_block">                        <span class="bp">self</span><span class="o">.</span><span class="n">serial</span><span class="o">.</span><span class="n">setDTR</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">dtr_state</span><span class="p">)</span>
</div><div id="l331" class="code_block">                        <span class="n">sys</span><span class="o">.</span><span class="n">stderr</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="s">&#39;--- DTR </span><span class="si">%s</span><span class="s"> ---</span><span class="se">\n</span><span class="s">&#39;</span> <span class="o">%</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">dtr_state</span> <span class="ow">and</span> <span class="s">&#39;active&#39;</span> <span class="ow">or</span> <span class="s">&#39;inactive&#39;</span><span class="p">))</span>
</div><div id="l332" class="code_block">                    <span class="k">elif</span> <span class="n">c</span> <span class="o">==</span> <span class="s">&#39;</span><span class="se">\x02</span><span class="s">&#39;</span><span class="p">:</span>                       <span class="c"># CTRL+B -&gt; toggle BREAK condition</span>
</div><div id="l333" class="code_block">                        <span class="bp">self</span><span class="o">.</span><span class="n">break_state</span> <span class="o">=</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">break_state</span>
</div><div id="l334" class="code_block">                        <span class="bp">self</span><span class="o">.</span><span class="n">serial</span><span class="o">.</span><span class="n">setBreak</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">break_state</span><span class="p">)</span>
</div><div id="l335" class="code_block">                        <span class="n">sys</span><span class="o">.</span><span class="n">stderr</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="s">&#39;--- BREAK </span><span class="si">%s</span><span class="s"> ---</span><span class="se">\n</span><span class="s">&#39;</span> <span class="o">%</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">break_state</span> <span class="ow">and</span> <span class="s">&#39;active&#39;</span> <span class="ow">or</span> <span class="s">&#39;inactive&#39;</span><span class="p">))</span>
</div><div id="l336" class="code_block">                    <span class="k">elif</span> <span class="n">c</span> <span class="o">==</span> <span class="s">&#39;</span><span class="se">\x05</span><span class="s">&#39;</span><span class="p">:</span>                       <span class="c"># CTRL+E -&gt; toggle local echo</span>
</div><div id="l337" class="code_block">                        <span class="bp">self</span><span class="o">.</span><span class="n">echo</span> <span class="o">=</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">echo</span>
</div><div id="l338" class="code_block">                        <span class="n">sys</span><span class="o">.</span><span class="n">stderr</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="s">&#39;--- local echo </span><span class="si">%s</span><span class="s"> ---</span><span class="se">\n</span><span class="s">&#39;</span> <span class="o">%</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">echo</span> <span class="ow">and</span> <span class="s">&#39;active&#39;</span> <span class="ow">or</span> <span class="s">&#39;inactive&#39;</span><span class="p">))</span>
</div><div id="l339" class="code_block">                    <span class="k">elif</span> <span class="n">c</span> <span class="o">==</span> <span class="s">&#39;</span><span class="se">\x09</span><span class="s">&#39;</span><span class="p">:</span>                       <span class="c"># CTRL+I -&gt; info</span>
</div><div id="l340" class="code_block">                        <span class="bp">self</span><span class="o">.</span><span class="n">dump_port_settings</span><span class="p">()</span>
</div><div id="l341" class="code_block">                    <span class="k">elif</span> <span class="n">c</span> <span class="o">==</span> <span class="s">&#39;</span><span class="se">\x01</span><span class="s">&#39;</span><span class="p">:</span>                       <span class="c"># CTRL+A -&gt; cycle escape mode</span>
</div><div id="l342" class="code_block">                        <span class="bp">self</span><span class="o">.</span><span class="n">repr_mode</span> <span class="o">+=</span> <span class="mi">1</span>
</div><div id="l343" class="code_block">                        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">repr_mode</span> <span class="o">&gt;</span> <span class="mi">3</span><span class="p">:</span>
</div><div id="l344" class="code_block">                            <span class="bp">self</span><span class="o">.</span><span class="n">repr_mode</span> <span class="o">=</span> <span class="mi">0</span>
</div><div id="l345" class="code_block">                        <span class="n">sys</span><span class="o">.</span><span class="n">stderr</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="s">&#39;--- escape data: </span><span class="si">%s</span><span class="s"> ---</span><span class="se">\n</span><span class="s">&#39;</span> <span class="o">%</span> <span class="p">(</span>
</div><div id="l346" class="code_block">                            <span class="n">REPR_MODES</span><span class="p">[</span><span class="bp">self</span><span class="o">.</span><span class="n">repr_mode</span><span class="p">],</span>
</div><div id="l347" class="code_block">                        <span class="p">))</span>
</div><div id="l348" class="code_block">                    <span class="k">elif</span> <span class="n">c</span> <span class="o">==</span> <span class="s">&#39;</span><span class="se">\x0c</span><span class="s">&#39;</span><span class="p">:</span>                       <span class="c"># CTRL+L -&gt; cycle linefeed mode</span>
</div><div id="l349" class="code_block">                        <span class="bp">self</span><span class="o">.</span><span class="n">convert_outgoing</span> <span class="o">+=</span> <span class="mi">1</span>
</div><div id="l350" class="code_block">                        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">convert_outgoing</span> <span class="o">&gt;</span> <span class="mi">2</span><span class="p">:</span>
</div><div id="l351" class="code_block">                            <span class="bp">self</span><span class="o">.</span><span class="n">convert_outgoing</span> <span class="o">=</span> <span class="mi">0</span>
</div><div id="l352" class="code_block">                        <span class="bp">self</span><span class="o">.</span><span class="n">newline</span> <span class="o">=</span> <span class="n">NEWLINE_CONVERISON_MAP</span><span class="p">[</span><span class="bp">self</span><span class="o">.</span><span class="n">convert_outgoing</span><span class="p">]</span>
</div><div id="l353" class="code_block">                        <span class="n">sys</span><span class="o">.</span><span class="n">stderr</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="s">&#39;--- line feed </span><span class="si">%s</span><span class="s"> ---</span><span class="se">\n</span><span class="s">&#39;</span> <span class="o">%</span> <span class="p">(</span>
</div><div id="l354" class="code_block">                            <span class="n">LF_MODES</span><span class="p">[</span><span class="bp">self</span><span class="o">.</span><span class="n">convert_outgoing</span><span class="p">],</span>
</div><div id="l355" class="code_block">                        <span class="p">))</span>
</div><div id="l356" class="code_block">                    <span class="k">elif</span> <span class="n">c</span> <span class="ow">in</span> <span class="s">&#39;pP&#39;</span><span class="p">:</span>                         <span class="c"># P -&gt; change port</span>
</div><div id="l357" class="code_block">                        <span class="n">dump_port_list</span><span class="p">()</span>
</div><div id="l358" class="code_block">                        <span class="n">sys</span><span class="o">.</span><span class="n">stderr</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="s">&#39;--- Enter port name: &#39;</span><span class="p">)</span>
</div><div id="l359" class="code_block">                        <span class="n">sys</span><span class="o">.</span><span class="n">stderr</span><span class="o">.</span><span class="n">flush</span><span class="p">()</span>
</div><div id="l360" class="code_block">                        <span class="n">console</span><span class="o">.</span><span class="n">cleanup</span><span class="p">()</span>
</div><div id="l361" class="code_block">                        <span class="k">try</span><span class="p">:</span>
</div><div id="l362" class="code_block">                            <span class="n">port</span> <span class="o">=</span> <span class="n">sys</span><span class="o">.</span><span class="n">stdin</span><span class="o">.</span><span class="n">readline</span><span class="p">()</span><span class="o">.</span><span class="n">strip</span><span class="p">()</span>
</div><div id="l363" class="code_block">                        <span class="k">except</span> <span class="ne">KeyboardInterrupt</span><span class="p">:</span>
</div><div id="l364" class="code_block">                            <span class="n">port</span> <span class="o">=</span> <span class="bp">None</span>
</div><div id="l365" class="code_block">                        <span class="n">console</span><span class="o">.</span><span class="n">setup</span><span class="p">()</span>
</div><div id="l366" class="code_block">                        <span class="k">if</span> <span class="n">port</span> <span class="ow">and</span> <span class="n">port</span> <span class="o">!=</span> <span class="bp">self</span><span class="o">.</span><span class="n">serial</span><span class="o">.</span><span class="n">port</span><span class="p">:</span>
</div><div id="l367" class="code_block">                            <span class="c"># reader thread needs to be shut down</span>
</div><div id="l368" class="code_block">                            <span class="bp">self</span><span class="o">.</span><span class="n">_stop_reader</span><span class="p">()</span>
</div><div id="l369" class="code_block">                            <span class="c"># save settings</span>
</div><div id="l370" class="code_block">                            <span class="n">settings</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">serial</span><span class="o">.</span><span class="n">getSettingsDict</span><span class="p">()</span>
</div><div id="l371" class="code_block">                            <span class="k">try</span><span class="p">:</span>
</div><div id="l372" class="code_block">                                <span class="k">try</span><span class="p">:</span>
</div><div id="l373" class="code_block">                                    <span class="n">new_serial</span> <span class="o">=</span> <span class="n">serial</span><span class="o">.</span><span class="n">serial_for_url</span><span class="p">(</span><span class="n">port</span><span class="p">,</span> <span class="n">do_not_open</span><span class="o">=</span><span class="bp">True</span><span class="p">)</span>
</div><div id="l374" class="code_block">                                <span class="k">except</span> <span class="ne">AttributeError</span><span class="p">:</span>
</div><div id="l375" class="code_block">                                    <span class="c"># happens when the installed pyserial is older than 2.5. use the</span>
</div><div id="l376" class="code_block">                                    <span class="c"># Serial class directly then.</span>
</div><div id="l377" class="code_block">                                    <span class="n">new_serial</span> <span class="o">=</span> <span class="n">serial</span><span class="o">.</span><span class="n">Serial</span><span class="p">()</span>
</div><div id="l378" class="code_block">                                    <span class="n">new_serial</span><span class="o">.</span><span class="n">port</span> <span class="o">=</span> <span class="n">port</span>
</div><div id="l379" class="code_block">                                <span class="c"># restore settings and open</span>
</div><div id="l380" class="code_block">                                <span class="n">new_serial</span><span class="o">.</span><span class="n">applySettingsDict</span><span class="p">(</span><span class="n">settings</span><span class="p">)</span>
</div><div id="l381" class="code_block">                                <span class="n">new_serial</span><span class="o">.</span><span class="n">open</span><span class="p">()</span>
</div><div id="l382" class="code_block">                                <span class="n">new_serial</span><span class="o">.</span><span class="n">setRTS</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">rts_state</span><span class="p">)</span>
</div><div id="l383" class="code_block">                                <span class="n">new_serial</span><span class="o">.</span><span class="n">setDTR</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">dtr_state</span><span class="p">)</span>
</div><div id="l384" class="code_block">                                <span class="n">new_serial</span><span class="o">.</span><span class="n">setBreak</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">break_state</span><span class="p">)</span>
</div><div id="l385" class="code_block">                            <span class="k">except</span> <span class="ne">Exception</span><span class="p">,</span> <span class="n">e</span><span class="p">:</span>
</div><div id="l386" class="code_block">                                <span class="n">sys</span><span class="o">.</span><span class="n">stderr</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="s">&#39;--- ERROR opening new port: </span><span class="si">%s</span><span class="s"> ---</span><span class="se">\n</span><span class="s">&#39;</span> <span class="o">%</span> <span class="p">(</span><span class="n">e</span><span class="p">,))</span>
</div><div id="l387" class="code_block">                                <span class="n">new_serial</span><span class="o">.</span><span class="n">close</span><span class="p">()</span>
</div><div id="l388" class="code_block">                            <span class="k">else</span><span class="p">:</span>
</div><div id="l389" class="code_block">                                <span class="bp">self</span><span class="o">.</span><span class="n">serial</span><span class="o">.</span><span class="n">close</span><span class="p">()</span>
</div><div id="l390" class="code_block">                                <span class="bp">self</span><span class="o">.</span><span class="n">serial</span> <span class="o">=</span> <span class="n">new_serial</span>
</div><div id="l391" class="code_block">                                <span class="n">sys</span><span class="o">.</span><span class="n">stderr</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="s">&#39;--- Port changed to: </span><span class="si">%s</span><span class="s"> ---</span><span class="se">\n</span><span class="s">&#39;</span> <span class="o">%</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">serial</span><span class="o">.</span><span class="n">port</span><span class="p">,))</span>
</div><div id="l392" class="code_block">                            <span class="c"># and restart the reader thread</span>
</div><div id="l393" class="code_block">                            <span class="bp">self</span><span class="o">.</span><span class="n">_start_reader</span><span class="p">()</span>
</div><div id="l394" class="code_block">                    <span class="k">elif</span> <span class="n">c</span> <span class="ow">in</span> <span class="s">&#39;bB&#39;</span><span class="p">:</span>                         <span class="c"># B -&gt; change baudrate</span>
</div><div id="l395" class="code_block">                        <span class="n">sys</span><span class="o">.</span><span class="n">stderr</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="s">&#39;</span><span class="se">\n</span><span class="s">--- Baudrate: &#39;</span><span class="p">)</span>
</div><div id="l396" class="code_block">                        <span class="n">sys</span><span class="o">.</span><span class="n">stderr</span><span class="o">.</span><span class="n">flush</span><span class="p">()</span>
</div><div id="l397" class="code_block">                        <span class="n">console</span><span class="o">.</span><span class="n">cleanup</span><span class="p">()</span>
</div><div id="l398" class="code_block">                        <span class="n">backup</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">serial</span><span class="o">.</span><span class="n">baudrate</span>
</div><div id="l399" class="code_block">                        <span class="k">try</span><span class="p">:</span>
</div><div id="l400" class="code_block">                            <span class="bp">self</span><span class="o">.</span><span class="n">serial</span><span class="o">.</span><span class="n">baudrate</span> <span class="o">=</span> <span class="nb">int</span><span class="p">(</span><span class="n">sys</span><span class="o">.</span><span class="n">stdin</span><span class="o">.</span><span class="n">readline</span><span class="p">()</span><span class="o">.</span><span class="n">strip</span><span class="p">())</span>
</div><div id="l401" class="code_block">                        <span class="k">except</span> <span class="ne">ValueError</span><span class="p">,</span> <span class="n">e</span><span class="p">:</span>
</div><div id="l402" class="code_block">                            <span class="n">sys</span><span class="o">.</span><span class="n">stderr</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="s">&#39;--- ERROR setting baudrate: </span><span class="si">%s</span><span class="s"> ---</span><span class="se">\n</span><span class="s">&#39;</span> <span class="o">%</span> <span class="p">(</span><span class="n">e</span><span class="p">,))</span>
</div><div id="l403" class="code_block">                            <span class="bp">self</span><span class="o">.</span><span class="n">serial</span><span class="o">.</span><span class="n">baudrate</span> <span class="o">=</span> <span class="n">backup</span>
</div><div id="l404" class="code_block">                        <span class="k">else</span><span class="p">:</span>
</div><div id="l405" class="code_block">                            <span class="bp">self</span><span class="o">.</span><span class="n">dump_port_settings</span><span class="p">()</span>
</div><div id="l406" class="code_block">                        <span class="n">console</span><span class="o">.</span><span class="n">setup</span><span class="p">()</span>
</div><div id="l407" class="code_block">                    <span class="k">elif</span> <span class="n">c</span> <span class="o">==</span> <span class="s">&#39;8&#39;</span><span class="p">:</span>                          <span class="c"># 8 -&gt; change to 8 bits</span>
</div><div id="l408" class="code_block">                        <span class="bp">self</span><span class="o">.</span><span class="n">serial</span><span class="o">.</span><span class="n">bytesize</span> <span class="o">=</span> <span class="n">serial</span><span class="o">.</span><span class="n">EIGHTBITS</span>
</div><div id="l409" class="code_block">                        <span class="bp">self</span><span class="o">.</span><span class="n">dump_port_settings</span><span class="p">()</span>
</div><div id="l410" class="code_block">                    <span class="k">elif</span> <span class="n">c</span> <span class="o">==</span> <span class="s">&#39;7&#39;</span><span class="p">:</span>                          <span class="c"># 7 -&gt; change to 8 bits</span>
</div><div id="l411" class="code_block">                        <span class="bp">self</span><span class="o">.</span><span class="n">serial</span><span class="o">.</span><span class="n">bytesize</span> <span class="o">=</span> <span class="n">serial</span><span class="o">.</span><span class="n">SEVENBITS</span>
</div><div id="l412" class="code_block">                        <span class="bp">self</span><span class="o">.</span><span class="n">dump_port_settings</span><span class="p">()</span>
</div><div id="l413" class="code_block">                    <span class="k">elif</span> <span class="n">c</span> <span class="ow">in</span> <span class="s">&#39;eE&#39;</span><span class="p">:</span>                         <span class="c"># E -&gt; change to even parity</span>
</div><div id="l414" class="code_block">                        <span class="bp">self</span><span class="o">.</span><span class="n">serial</span><span class="o">.</span><span class="n">parity</span> <span class="o">=</span> <span class="n">serial</span><span class="o">.</span><span class="n">PARITY_EVEN</span>
</div><div id="l415" class="code_block">                        <span class="bp">self</span><span class="o">.</span><span class="n">dump_port_settings</span><span class="p">()</span>
</div><div id="l416" class="code_block">                    <span class="k">elif</span> <span class="n">c</span> <span class="ow">in</span> <span class="s">&#39;oO&#39;</span><span class="p">:</span>                         <span class="c"># O -&gt; change to odd parity</span>
</div><div id="l417" class="code_block">                        <span class="bp">self</span><span class="o">.</span><span class="n">serial</span><span class="o">.</span><span class="n">parity</span> <span class="o">=</span> <span class="n">serial</span><span class="o">.</span><span class="n">PARITY_ODD</span>
</div><div id="l418" class="code_block">                        <span class="bp">self</span><span class="o">.</span><span class="n">dump_port_settings</span><span class="p">()</span>
</div><div id="l419" class="code_block">                    <span class="k">elif</span> <span class="n">c</span> <span class="ow">in</span> <span class="s">&#39;mM&#39;</span><span class="p">:</span>                         <span class="c"># M -&gt; change to mark parity</span>
</div><div id="l420" class="code_block">                        <span class="bp">self</span><span class="o">.</span><span class="n">serial</span><span class="o">.</span><span class="n">parity</span> <span class="o">=</span> <span class="n">serial</span><span class="o">.</span><span class="n">PARITY_MARK</span>
</div><div id="l421" class="code_block">                        <span class="bp">self</span><span class="o">.</span><span class="n">dump_port_settings</span><span class="p">()</span>
</div><div id="l422" class="code_block">                    <span class="k">elif</span> <span class="n">c</span> <span class="ow">in</span> <span class="s">&#39;sS&#39;</span><span class="p">:</span>                         <span class="c"># S -&gt; change to space parity</span>
</div><div id="l423" class="code_block">                        <span class="bp">self</span><span class="o">.</span><span class="n">serial</span><span class="o">.</span><span class="n">parity</span> <span class="o">=</span> <span class="n">serial</span><span class="o">.</span><span class="n">PARITY_SPACE</span>
</div><div id="l424" class="code_block">                        <span class="bp">self</span><span class="o">.</span><span class="n">dump_port_settings</span><span class="p">()</span>
</div><div id="l425" class="code_block">                    <span class="k">elif</span> <span class="n">c</span> <span class="ow">in</span> <span class="s">&#39;nN&#39;</span><span class="p">:</span>                         <span class="c"># N -&gt; change to no parity</span>
</div><div id="l426" class="code_block">                        <span class="bp">self</span><span class="o">.</span><span class="n">serial</span><span class="o">.</span><span class="n">parity</span> <span class="o">=</span> <span class="n">serial</span><span class="o">.</span><span class="n">PARITY_NONE</span>
</div><div id="l427" class="code_block">                        <span class="bp">self</span><span class="o">.</span><span class="n">dump_port_settings</span><span class="p">()</span>
</div><div id="l428" class="code_block">                    <span class="k">elif</span> <span class="n">c</span> <span class="o">==</span> <span class="s">&#39;1&#39;</span><span class="p">:</span>                          <span class="c"># 1 -&gt; change to 1 stop bits</span>
</div><div id="l429" class="code_block">                        <span class="bp">self</span><span class="o">.</span><span class="n">serial</span><span class="o">.</span><span class="n">stopbits</span> <span class="o">=</span> <span class="n">serial</span><span class="o">.</span><span class="n">STOPBITS_ONE</span>
</div><div id="l430" class="code_block">                        <span class="bp">self</span><span class="o">.</span><span class="n">dump_port_settings</span><span class="p">()</span>
</div><div id="l431" class="code_block">                    <span class="k">elif</span> <span class="n">c</span> <span class="o">==</span> <span class="s">&#39;2&#39;</span><span class="p">:</span>                          <span class="c"># 2 -&gt; change to 2 stop bits</span>
</div><div id="l432" class="code_block">                        <span class="bp">self</span><span class="o">.</span><span class="n">serial</span><span class="o">.</span><span class="n">stopbits</span> <span class="o">=</span> <span class="n">serial</span><span class="o">.</span><span class="n">STOPBITS_TWO</span>
</div><div id="l433" class="code_block">                        <span class="bp">self</span><span class="o">.</span><span class="n">dump_port_settings</span><span class="p">()</span>
</div><div id="l434" class="code_block">                    <span class="k">elif</span> <span class="n">c</span> <span class="o">==</span> <span class="s">&#39;3&#39;</span><span class="p">:</span>                          <span class="c"># 3 -&gt; change to 1.5 stop bits</span>
</div><div id="l435" class="code_block">                        <span class="bp">self</span><span class="o">.</span><span class="n">serial</span><span class="o">.</span><span class="n">stopbits</span> <span class="o">=</span> <span class="n">serial</span><span class="o">.</span><span class="n">STOPBITS_ONE_POINT_FIVE</span>
</div><div id="l436" class="code_block">                        <span class="bp">self</span><span class="o">.</span><span class="n">dump_port_settings</span><span class="p">()</span>
</div><div id="l437" class="code_block">                    <span class="k">elif</span> <span class="n">c</span> <span class="ow">in</span> <span class="s">&#39;xX&#39;</span><span class="p">:</span>                         <span class="c"># X -&gt; change software flow control</span>
</div><div id="l438" class="code_block">                        <span class="bp">self</span><span class="o">.</span><span class="n">serial</span><span class="o">.</span><span class="n">xonxoff</span> <span class="o">=</span> <span class="p">(</span><span class="n">c</span> <span class="o">==</span> <span class="s">&#39;X&#39;</span><span class="p">)</span>
</div><div id="l439" class="code_block">                        <span class="bp">self</span><span class="o">.</span><span class="n">dump_port_settings</span><span class="p">()</span>
</div><div id="l440" class="code_block">                    <span class="k">elif</span> <span class="n">c</span> <span class="ow">in</span> <span class="s">&#39;rR&#39;</span><span class="p">:</span>                         <span class="c"># R -&gt; change hardware flow control</span>
</div><div id="l441" class="code_block">                        <span class="bp">self</span><span class="o">.</span><span class="n">serial</span><span class="o">.</span><span class="n">rtscts</span> <span class="o">=</span> <span class="p">(</span><span class="n">c</span> <span class="o">==</span> <span class="s">&#39;R&#39;</span><span class="p">)</span>
</div><div id="l442" class="code_block">                        <span class="bp">self</span><span class="o">.</span><span class="n">dump_port_settings</span><span class="p">()</span>
</div><div id="l443" class="code_block">                    <span class="k">else</span><span class="p">:</span>
</div><div id="l444" class="code_block">                        <span class="n">sys</span><span class="o">.</span><span class="n">stderr</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="s">&#39;--- unknown menu character </span><span class="si">%s</span><span class="s"> --</span><span class="se">\n</span><span class="s">&#39;</span> <span class="o">%</span> <span class="n">key_description</span><span class="p">(</span><span class="n">c</span><span class="p">))</span>
</div><div id="l445" class="code_block">                    <span class="n">menu_active</span> <span class="o">=</span> <span class="bp">False</span>
</div><div id="l446" class="code_block">                <span class="k">elif</span> <span class="n">c</span> <span class="o">==</span> <span class="n">MENUCHARACTER</span><span class="p">:</span> <span class="c"># next char will be for menu</span>
</div><div id="l447" class="code_block">                    <span class="n">menu_active</span> <span class="o">=</span> <span class="bp">True</span>
</div><div id="l448" class="code_block">                <span class="k">elif</span> <span class="n">c</span> <span class="o">==</span> <span class="n">EXITCHARCTER</span><span class="p">:</span> 
</div><div id="l449" class="code_block">                    <span class="bp">self</span><span class="o">.</span><span class="n">stop</span><span class="p">()</span>
</div><div id="l450" class="code_block">                    <span class="k">break</span>                                   <span class="c"># exit app</span>
</div><div id="l451" class="code_block">                <span class="k">elif</span> <span class="n">c</span> <span class="o">==</span> <span class="s">&#39;</span><span class="se">\n</span><span class="s">&#39;</span><span class="p">:</span>
</div><div id="l452" class="code_block">                    <span class="bp">self</span><span class="o">.</span><span class="n">serial</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">newline</span><span class="p">)</span>         <span class="c"># send newline character(s)</span>
</div><div id="l453" class="code_block">                    <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">echo</span><span class="p">:</span>
</div><div id="l454" class="code_block">                        <span class="n">sys</span><span class="o">.</span><span class="n">stdout</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="n">c</span><span class="p">)</span>                 <span class="c"># local echo is a real newline in any case</span>
</div><div id="l455" class="code_block">                        <span class="n">sys</span><span class="o">.</span><span class="n">stdout</span><span class="o">.</span><span class="n">flush</span><span class="p">()</span>
</div><div id="l456" class="code_block">                <span class="k">else</span><span class="p">:</span>
</div><div id="l457" class="code_block">                    <span class="bp">self</span><span class="o">.</span><span class="n">serial</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="n">b</span><span class="p">)</span>                    <span class="c"># send byte</span>
</div><div id="l458" class="code_block">                    <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">echo</span><span class="p">:</span>
</div><div id="l459" class="code_block">                        <span class="n">sys</span><span class="o">.</span><span class="n">stdout</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="n">c</span><span class="p">)</span>
</div><div id="l460" class="code_block">                        <span class="n">sys</span><span class="o">.</span><span class="n">stdout</span><span class="o">.</span><span class="n">flush</span><span class="p">()</span>
</div><div id="l461" class="code_block">        <span class="k">except</span><span class="p">:</span>
</div><div id="l462" class="code_block">            <span class="bp">self</span><span class="o">.</span><span class="n">alive</span> <span class="o">=</span> <span class="bp">False</span>
</div><div id="l463" class="code_block">            <span class="k">raise</span>
</div><div id="l464" class="code_block">
</div><div id="l465" class="code_block"><span class="k">def</span> <span class="nf">main</span><span class="p">():</span>
</div><div id="l466" class="code_block">    <span class="kn">import</span> <span class="nn">optparse</span>
</div><div id="l467" class="code_block">
</div><div id="l468" class="code_block">    <span class="n">parser</span> <span class="o">=</span> <span class="n">optparse</span><span class="o">.</span><span class="n">OptionParser</span><span class="p">(</span>
</div><div id="l469" class="code_block">        <span class="n">usage</span> <span class="o">=</span> <span class="s">&quot;%prog [options] [port [baudrate]]&quot;</span><span class="p">,</span>
</div><div id="l470" class="code_block">        <span class="n">description</span> <span class="o">=</span> <span class="s">&quot;Miniterm - A simple terminal program for the serial port.&quot;</span>
</div><div id="l471" class="code_block">    <span class="p">)</span>
</div><div id="l472" class="code_block">
</div><div id="l473" class="code_block">    <span class="n">group</span> <span class="o">=</span> <span class="n">optparse</span><span class="o">.</span><span class="n">OptionGroup</span><span class="p">(</span><span class="n">parser</span><span class="p">,</span> <span class="s">&quot;Port settings&quot;</span><span class="p">)</span>
</div><div id="l474" class="code_block">
</div><div id="l475" class="code_block">    <span class="n">group</span><span class="o">.</span><span class="n">add_option</span><span class="p">(</span><span class="s">&quot;-p&quot;</span><span class="p">,</span> <span class="s">&quot;--port&quot;</span><span class="p">,</span>
</div><div id="l476" class="code_block">        <span class="n">dest</span> <span class="o">=</span> <span class="s">&quot;port&quot;</span><span class="p">,</span>
</div><div id="l477" class="code_block">        <span class="n">help</span> <span class="o">=</span> <span class="s">&quot;port, a number or a device name. (deprecated option, use parameter instead)&quot;</span><span class="p">,</span>
</div><div id="l478" class="code_block">        <span class="n">default</span> <span class="o">=</span> <span class="n">DEFAULT_PORT</span>
</div><div id="l479" class="code_block">    <span class="p">)</span>
</div><div id="l480" class="code_block">
</div><div id="l481" class="code_block">    <span class="n">group</span><span class="o">.</span><span class="n">add_option</span><span class="p">(</span><span class="s">&quot;-b&quot;</span><span class="p">,</span> <span class="s">&quot;--baud&quot;</span><span class="p">,</span>
</div><div id="l482" class="code_block">        <span class="n">dest</span> <span class="o">=</span> <span class="s">&quot;baudrate&quot;</span><span class="p">,</span>
</div><div id="l483" class="code_block">        <span class="n">action</span> <span class="o">=</span> <span class="s">&quot;store&quot;</span><span class="p">,</span>
</div><div id="l484" class="code_block">        <span class="nb">type</span> <span class="o">=</span> <span class="s">&#39;int&#39;</span><span class="p">,</span>
</div><div id="l485" class="code_block">        <span class="n">help</span> <span class="o">=</span> <span class="s">&quot;set baud rate, default </span><span class="si">%d</span><span class="s">efault&quot;</span><span class="p">,</span>
</div><div id="l486" class="code_block">        <span class="n">default</span> <span class="o">=</span> <span class="n">DEFAULT_BAUDRATE</span>
</div><div id="l487" class="code_block">    <span class="p">)</span>
</div><div id="l488" class="code_block">
</div><div id="l489" class="code_block">    <span class="n">group</span><span class="o">.</span><span class="n">add_option</span><span class="p">(</span><span class="s">&quot;--parity&quot;</span><span class="p">,</span>
</div><div id="l490" class="code_block">        <span class="n">dest</span> <span class="o">=</span> <span class="s">&quot;parity&quot;</span><span class="p">,</span>
</div><div id="l491" class="code_block">        <span class="n">action</span> <span class="o">=</span> <span class="s">&quot;store&quot;</span><span class="p">,</span>
</div><div id="l492" class="code_block">        <span class="n">help</span> <span class="o">=</span> <span class="s">&quot;set parity, one of [N, E, O, S, M], default=N&quot;</span><span class="p">,</span>
</div><div id="l493" class="code_block">        <span class="n">default</span> <span class="o">=</span> <span class="s">&#39;N&#39;</span>
</div><div id="l494" class="code_block">    <span class="p">)</span>
</div><div id="l495" class="code_block">
</div><div id="l496" class="code_block">    <span class="n">group</span><span class="o">.</span><span class="n">add_option</span><span class="p">(</span><span class="s">&quot;--rtscts&quot;</span><span class="p">,</span>
</div><div id="l497" class="code_block">        <span class="n">dest</span> <span class="o">=</span> <span class="s">&quot;rtscts&quot;</span><span class="p">,</span>
</div><div id="l498" class="code_block">        <span class="n">action</span> <span class="o">=</span> <span class="s">&quot;store_true&quot;</span><span class="p">,</span>
</div><div id="l499" class="code_block">        <span class="n">help</span> <span class="o">=</span> <span class="s">&quot;enable RTS/CTS flow control (default off)&quot;</span><span class="p">,</span>
</div><div id="l500" class="code_block">        <span class="n">default</span> <span class="o">=</span> <span class="bp">False</span>
</div><div id="l501" class="code_block">    <span class="p">)</span>
</div><div id="l502" class="code_block">
</div><div id="l503" class="code_block">    <span class="n">group</span><span class="o">.</span><span class="n">add_option</span><span class="p">(</span><span class="s">&quot;--xonxoff&quot;</span><span class="p">,</span>
</div><div id="l504" class="code_block">        <span class="n">dest</span> <span class="o">=</span> <span class="s">&quot;xonxoff&quot;</span><span class="p">,</span>
</div><div id="l505" class="code_block">        <span class="n">action</span> <span class="o">=</span> <span class="s">&quot;store_true&quot;</span><span class="p">,</span>
</div><div id="l506" class="code_block">        <span class="n">help</span> <span class="o">=</span> <span class="s">&quot;enable software flow control (default off)&quot;</span><span class="p">,</span>
</div><div id="l507" class="code_block">        <span class="n">default</span> <span class="o">=</span> <span class="bp">False</span>
</div><div id="l508" class="code_block">    <span class="p">)</span>
</div><div id="l509" class="code_block">
</div><div id="l510" class="code_block">    <span class="n">group</span><span class="o">.</span><span class="n">add_option</span><span class="p">(</span><span class="s">&quot;--rts&quot;</span><span class="p">,</span>
</div><div id="l511" class="code_block">        <span class="n">dest</span> <span class="o">=</span> <span class="s">&quot;rts_state&quot;</span><span class="p">,</span>
</div><div id="l512" class="code_block">        <span class="n">action</span> <span class="o">=</span> <span class="s">&quot;store&quot;</span><span class="p">,</span>
</div><div id="l513" class="code_block">        <span class="nb">type</span> <span class="o">=</span> <span class="s">&#39;int&#39;</span><span class="p">,</span>
</div><div id="l514" class="code_block">        <span class="n">help</span> <span class="o">=</span> <span class="s">&quot;set initial RTS line state (possible values: 0, 1)&quot;</span><span class="p">,</span>
</div><div id="l515" class="code_block">        <span class="n">default</span> <span class="o">=</span> <span class="n">DEFAULT_RTS</span>
</div><div id="l516" class="code_block">    <span class="p">)</span>
</div><div id="l517" class="code_block">
</div><div id="l518" class="code_block">    <span class="n">group</span><span class="o">.</span><span class="n">add_option</span><span class="p">(</span><span class="s">&quot;--dtr&quot;</span><span class="p">,</span>
</div><div id="l519" class="code_block">        <span class="n">dest</span> <span class="o">=</span> <span class="s">&quot;dtr_state&quot;</span><span class="p">,</span>
</div><div id="l520" class="code_block">        <span class="n">action</span> <span class="o">=</span> <span class="s">&quot;store&quot;</span><span class="p">,</span>
</div><div id="l521" class="code_block">        <span class="nb">type</span> <span class="o">=</span> <span class="s">&#39;int&#39;</span><span class="p">,</span>
</div><div id="l522" class="code_block">        <span class="n">help</span> <span class="o">=</span> <span class="s">&quot;set initial DTR line state (possible values: 0, 1)&quot;</span><span class="p">,</span>
</div><div id="l523" class="code_block">        <span class="n">default</span> <span class="o">=</span> <span class="n">DEFAULT_DTR</span>
</div><div id="l524" class="code_block">    <span class="p">)</span>
</div><div id="l525" class="code_block">
</div><div id="l526" class="code_block">    <span class="n">parser</span><span class="o">.</span><span class="n">add_option_group</span><span class="p">(</span><span class="n">group</span><span class="p">)</span>
</div><div id="l527" class="code_block">
</div><div id="l528" class="code_block">    <span class="n">group</span> <span class="o">=</span> <span class="n">optparse</span><span class="o">.</span><span class="n">OptionGroup</span><span class="p">(</span><span class="n">parser</span><span class="p">,</span> <span class="s">&quot;Data handling&quot;</span><span class="p">)</span>
</div><div id="l529" class="code_block">
</div><div id="l530" class="code_block">    <span class="n">group</span><span class="o">.</span><span class="n">add_option</span><span class="p">(</span><span class="s">&quot;-e&quot;</span><span class="p">,</span> <span class="s">&quot;--echo&quot;</span><span class="p">,</span>
</div><div id="l531" class="code_block">        <span class="n">dest</span> <span class="o">=</span> <span class="s">&quot;echo&quot;</span><span class="p">,</span>
</div><div id="l532" class="code_block">        <span class="n">action</span> <span class="o">=</span> <span class="s">&quot;store_true&quot;</span><span class="p">,</span>
</div><div id="l533" class="code_block">        <span class="n">help</span> <span class="o">=</span> <span class="s">&quot;enable local echo (default off)&quot;</span><span class="p">,</span>
</div><div id="l534" class="code_block">        <span class="n">default</span> <span class="o">=</span> <span class="bp">False</span>
</div><div id="l535" class="code_block">    <span class="p">)</span>
</div><div id="l536" class="code_block">
</div><div id="l537" class="code_block">    <span class="n">group</span><span class="o">.</span><span class="n">add_option</span><span class="p">(</span><span class="s">&quot;--cr&quot;</span><span class="p">,</span>
</div><div id="l538" class="code_block">        <span class="n">dest</span> <span class="o">=</span> <span class="s">&quot;cr&quot;</span><span class="p">,</span>
</div><div id="l539" class="code_block">        <span class="n">action</span> <span class="o">=</span> <span class="s">&quot;store_true&quot;</span><span class="p">,</span>
</div><div id="l540" class="code_block">        <span class="n">help</span> <span class="o">=</span> <span class="s">&quot;do not send CR+LF, send CR only&quot;</span><span class="p">,</span>
</div><div id="l541" class="code_block">        <span class="n">default</span> <span class="o">=</span> <span class="bp">False</span>
</div><div id="l542" class="code_block">    <span class="p">)</span>
</div><div id="l543" class="code_block">
</div><div id="l544" class="code_block">    <span class="n">group</span><span class="o">.</span><span class="n">add_option</span><span class="p">(</span><span class="s">&quot;--lf&quot;</span><span class="p">,</span>
</div><div id="l545" class="code_block">        <span class="n">dest</span> <span class="o">=</span> <span class="s">&quot;lf&quot;</span><span class="p">,</span>
</div><div id="l546" class="code_block">        <span class="n">action</span> <span class="o">=</span> <span class="s">&quot;store_true&quot;</span><span class="p">,</span>
</div><div id="l547" class="code_block">        <span class="n">help</span> <span class="o">=</span> <span class="s">&quot;do not send CR+LF, send LF only&quot;</span><span class="p">,</span>
</div><div id="l548" class="code_block">        <span class="n">default</span> <span class="o">=</span> <span class="bp">False</span>
</div><div id="l549" class="code_block">    <span class="p">)</span>
</div><div id="l550" class="code_block">
</div><div id="l551" class="code_block">    <span class="n">group</span><span class="o">.</span><span class="n">add_option</span><span class="p">(</span><span class="s">&quot;-D&quot;</span><span class="p">,</span> <span class="s">&quot;--debug&quot;</span><span class="p">,</span>
</div><div id="l552" class="code_block">        <span class="n">dest</span> <span class="o">=</span> <span class="s">&quot;repr_mode&quot;</span><span class="p">,</span>
</div><div id="l553" class="code_block">        <span class="n">action</span> <span class="o">=</span> <span class="s">&quot;count&quot;</span><span class="p">,</span>
</div><div id="l554" class="code_block">        <span class="n">help</span> <span class="o">=</span> <span class="s">&quot;&quot;&quot;debug received data (escape non-printable chars)</span>
</div><div id="l555" class="code_block"><span class="s">--debug can be given multiple times:</span>
</div><div id="l556" class="code_block"><span class="s">0: just print what is received</span>
</div><div id="l557" class="code_block"><span class="s">1: escape non-printable characters, do newlines as unusual</span>
</div><div id="l558" class="code_block"><span class="s">2: escape non-printable characters, newlines too</span>
</div><div id="l559" class="code_block"><span class="s">3: hex dump everything&quot;&quot;&quot;</span><span class="p">,</span>
</div><div id="l560" class="code_block">        <span class="n">default</span> <span class="o">=</span> <span class="mi">0</span>
</div><div id="l561" class="code_block">    <span class="p">)</span>
</div><div id="l562" class="code_block">
</div><div id="l563" class="code_block">    <span class="n">parser</span><span class="o">.</span><span class="n">add_option_group</span><span class="p">(</span><span class="n">group</span><span class="p">)</span>
</div><div id="l564" class="code_block">
</div><div id="l565" class="code_block">
</div><div id="l566" class="code_block">    <span class="n">group</span> <span class="o">=</span> <span class="n">optparse</span><span class="o">.</span><span class="n">OptionGroup</span><span class="p">(</span><span class="n">parser</span><span class="p">,</span> <span class="s">&quot;Hotkeys&quot;</span><span class="p">)</span>
</div><div id="l567" class="code_block">
</div><div id="l568" class="code_block">    <span class="n">group</span><span class="o">.</span><span class="n">add_option</span><span class="p">(</span><span class="s">&quot;--exit-char&quot;</span><span class="p">,</span>
</div><div id="l569" class="code_block">        <span class="n">dest</span> <span class="o">=</span> <span class="s">&quot;exit_char&quot;</span><span class="p">,</span>
</div><div id="l570" class="code_block">        <span class="n">action</span> <span class="o">=</span> <span class="s">&quot;store&quot;</span><span class="p">,</span>
</div><div id="l571" class="code_block">        <span class="nb">type</span> <span class="o">=</span> <span class="s">&#39;int&#39;</span><span class="p">,</span>
</div><div id="l572" class="code_block">        <span class="n">help</span> <span class="o">=</span> <span class="s">&quot;ASCII code of special character that is used to exit the application&quot;</span><span class="p">,</span>
</div><div id="l573" class="code_block">        <span class="n">default</span> <span class="o">=</span> <span class="mh">0x1d</span>
</div><div id="l574" class="code_block">    <span class="p">)</span>
</div><div id="l575" class="code_block">
</div><div id="l576" class="code_block">    <span class="n">group</span><span class="o">.</span><span class="n">add_option</span><span class="p">(</span><span class="s">&quot;--menu-char&quot;</span><span class="p">,</span>
</div><div id="l577" class="code_block">        <span class="n">dest</span> <span class="o">=</span> <span class="s">&quot;menu_char&quot;</span><span class="p">,</span>
</div><div id="l578" class="code_block">        <span class="n">action</span> <span class="o">=</span> <span class="s">&quot;store&quot;</span><span class="p">,</span>
</div><div id="l579" class="code_block">        <span class="nb">type</span> <span class="o">=</span> <span class="s">&#39;int&#39;</span><span class="p">,</span>
</div><div id="l580" class="code_block">        <span class="n">help</span> <span class="o">=</span> <span class="s">&quot;ASCII code of special character that is used to control miniterm (menu)&quot;</span><span class="p">,</span>
</div><div id="l581" class="code_block">        <span class="n">default</span> <span class="o">=</span> <span class="mh">0x14</span>
</div><div id="l582" class="code_block">    <span class="p">)</span>
</div><div id="l583" class="code_block">
</div><div id="l584" class="code_block">    <span class="n">parser</span><span class="o">.</span><span class="n">add_option_group</span><span class="p">(</span><span class="n">group</span><span class="p">)</span>
</div><div id="l585" class="code_block">
</div><div id="l586" class="code_block">    <span class="n">group</span> <span class="o">=</span> <span class="n">optparse</span><span class="o">.</span><span class="n">OptionGroup</span><span class="p">(</span><span class="n">parser</span><span class="p">,</span> <span class="s">&quot;Diagnostics&quot;</span><span class="p">)</span>
</div><div id="l587" class="code_block">
</div><div id="l588" class="code_block">    <span class="n">group</span><span class="o">.</span><span class="n">add_option</span><span class="p">(</span><span class="s">&quot;-q&quot;</span><span class="p">,</span> <span class="s">&quot;--quiet&quot;</span><span class="p">,</span>
</div><div id="l589" class="code_block">        <span class="n">dest</span> <span class="o">=</span> <span class="s">&quot;quiet&quot;</span><span class="p">,</span>
</div><div id="l590" class="code_block">        <span class="n">action</span> <span class="o">=</span> <span class="s">&quot;store_true&quot;</span><span class="p">,</span>
</div><div id="l591" class="code_block">        <span class="n">help</span> <span class="o">=</span> <span class="s">&quot;suppress non-error messages&quot;</span><span class="p">,</span>
</div><div id="l592" class="code_block">        <span class="n">default</span> <span class="o">=</span> <span class="bp">False</span>
</div><div id="l593" class="code_block">    <span class="p">)</span>
</div><div id="l594" class="code_block">
</div><div id="l595" class="code_block">    <span class="n">parser</span><span class="o">.</span><span class="n">add_option_group</span><span class="p">(</span><span class="n">group</span><span class="p">)</span>
</div><div id="l596" class="code_block">
</div><div id="l597" class="code_block">
</div><div id="l598" class="code_block">    <span class="p">(</span><span class="n">options</span><span class="p">,</span> <span class="n">args</span><span class="p">)</span> <span class="o">=</span> <span class="n">parser</span><span class="o">.</span><span class="n">parse_args</span><span class="p">()</span>
</div><div id="l599" class="code_block">
</div><div id="l600" class="code_block">    <span class="n">options</span><span class="o">.</span><span class="n">parity</span> <span class="o">=</span> <span class="n">options</span><span class="o">.</span><span class="n">parity</span><span class="o">.</span><span class="n">upper</span><span class="p">()</span>
</div><div id="l601" class="code_block">    <span class="k">if</span> <span class="n">options</span><span class="o">.</span><span class="n">parity</span> <span class="ow">not</span> <span class="ow">in</span> <span class="s">&#39;NEOSM&#39;</span><span class="p">:</span>
</div><div id="l602" class="code_block">        <span class="n">parser</span><span class="o">.</span><span class="n">error</span><span class="p">(</span><span class="s">&quot;invalid parity&quot;</span><span class="p">)</span>
</div><div id="l603" class="code_block">
</div><div id="l604" class="code_block">    <span class="k">if</span> <span class="n">options</span><span class="o">.</span><span class="n">cr</span> <span class="ow">and</span> <span class="n">options</span><span class="o">.</span><span class="n">lf</span><span class="p">:</span>
</div><div id="l605" class="code_block">        <span class="n">parser</span><span class="o">.</span><span class="n">error</span><span class="p">(</span><span class="s">&quot;only one of --cr or --lf can be specified&quot;</span><span class="p">)</span>
</div><div id="l606" class="code_block">
</div><div id="l607" class="code_block">    <span class="k">if</span> <span class="n">options</span><span class="o">.</span><span class="n">menu_char</span> <span class="o">==</span> <span class="n">options</span><span class="o">.</span><span class="n">exit_char</span><span class="p">:</span>
</div><div id="l608" class="code_block">        <span class="n">parser</span><span class="o">.</span><span class="n">error</span><span class="p">(</span><span class="s">&#39;--exit-char can not be the same as --menu-char&#39;</span><span class="p">)</span>
</div><div id="l609" class="code_block">
</div><div id="l610" class="code_block">    <span class="k">global</span> <span class="n">EXITCHARCTER</span><span class="p">,</span> <span class="n">MENUCHARACTER</span>
</div><div id="l611" class="code_block">    <span class="n">EXITCHARCTER</span> <span class="o">=</span> <span class="nb">chr</span><span class="p">(</span><span class="n">options</span><span class="o">.</span><span class="n">exit_char</span><span class="p">)</span>
</div><div id="l612" class="code_block">    <span class="n">MENUCHARACTER</span> <span class="o">=</span> <span class="nb">chr</span><span class="p">(</span><span class="n">options</span><span class="o">.</span><span class="n">menu_char</span><span class="p">)</span>
</div><div id="l613" class="code_block">
</div><div id="l614" class="code_block">    <span class="n">port</span> <span class="o">=</span> <span class="n">options</span><span class="o">.</span><span class="n">port</span>
</div><div id="l615" class="code_block">    <span class="n">baudrate</span> <span class="o">=</span> <span class="n">options</span><span class="o">.</span><span class="n">baudrate</span>
</div><div id="l616" class="code_block">    <span class="k">if</span> <span class="n">args</span><span class="p">:</span>
</div><div id="l617" class="code_block">        <span class="k">if</span> <span class="n">options</span><span class="o">.</span><span class="n">port</span> <span class="ow">is</span> <span class="ow">not</span> <span class="bp">None</span><span class="p">:</span>
</div><div id="l618" class="code_block">            <span class="n">parser</span><span class="o">.</span><span class="n">error</span><span class="p">(</span><span class="s">&quot;no arguments are allowed, options only when --port is given&quot;</span><span class="p">)</span>
</div><div id="l619" class="code_block">        <span class="n">port</span> <span class="o">=</span> <span class="n">args</span><span class="o">.</span><span class="n">pop</span><span class="p">(</span><span class="mi">0</span><span class="p">)</span>
</div><div id="l620" class="code_block">        <span class="k">if</span> <span class="n">args</span><span class="p">:</span>
</div><div id="l621" class="code_block">            <span class="k">try</span><span class="p">:</span>
</div><div id="l622" class="code_block">                <span class="n">baudrate</span> <span class="o">=</span> <span class="nb">int</span><span class="p">(</span><span class="n">args</span><span class="p">[</span><span class="mi">0</span><span class="p">])</span>
</div><div id="l623" class="code_block">            <span class="k">except</span> <span class="ne">ValueError</span><span class="p">:</span>
</div><div id="l624" class="code_block">                <span class="n">parser</span><span class="o">.</span><span class="n">error</span><span class="p">(</span><span class="s">&quot;baud rate must be a number, not </span><span class="si">%r</span><span class="s">&quot;</span> <span class="o">%</span> <span class="n">args</span><span class="p">[</span><span class="mi">0</span><span class="p">])</span>
</div><div id="l625" class="code_block">            <span class="n">args</span><span class="o">.</span><span class="n">pop</span><span class="p">(</span><span class="mi">0</span><span class="p">)</span>
</div><div id="l626" class="code_block">        <span class="k">if</span> <span class="n">args</span><span class="p">:</span>
</div><div id="l627" class="code_block">            <span class="n">parser</span><span class="o">.</span><span class="n">error</span><span class="p">(</span><span class="s">&quot;too many arguments&quot;</span><span class="p">)</span>
</div><div id="l628" class="code_block">    <span class="k">else</span><span class="p">:</span>
</div><div id="l629" class="code_block">        <span class="c"># no port given on command line -&gt; ask user now</span>
</div><div id="l630" class="code_block">        <span class="k">if</span> <span class="n">port</span> <span class="ow">is</span> <span class="bp">None</span><span class="p">:</span>
</div><div id="l631" class="code_block">            <span class="n">dump_port_list</span><span class="p">()</span>
</div><div id="l632" class="code_block">            <span class="n">port</span> <span class="o">=</span> <span class="nb">raw_input</span><span class="p">(</span><span class="s">&#39;Enter port name:&#39;</span><span class="p">)</span>
</div><div id="l633" class="code_block">
</div><div id="l634" class="code_block">    <span class="n">convert_outgoing</span> <span class="o">=</span> <span class="n">CONVERT_CRLF</span>
</div><div id="l635" class="code_block">    <span class="k">if</span> <span class="n">options</span><span class="o">.</span><span class="n">cr</span><span class="p">:</span>
</div><div id="l636" class="code_block">        <span class="n">convert_outgoing</span> <span class="o">=</span> <span class="n">CONVERT_CR</span>
</div><div id="l637" class="code_block">    <span class="k">elif</span> <span class="n">options</span><span class="o">.</span><span class="n">lf</span><span class="p">:</span>
</div><div id="l638" class="code_block">        <span class="n">convert_outgoing</span> <span class="o">=</span> <span class="n">CONVERT_LF</span>
</div><div id="l639" class="code_block">
</div><div id="l640" class="code_block">    <span class="k">try</span><span class="p">:</span>
</div><div id="l641" class="code_block">        <span class="n">miniterm</span> <span class="o">=</span> <span class="n">Miniterm</span><span class="p">(</span>
</div><div id="l642" class="code_block">            <span class="n">port</span><span class="p">,</span>
</div><div id="l643" class="code_block">            <span class="n">baudrate</span><span class="p">,</span>
</div><div id="l644" class="code_block">            <span class="n">options</span><span class="o">.</span><span class="n">parity</span><span class="p">,</span>
</div><div id="l645" class="code_block">            <span class="n">rtscts</span><span class="o">=</span><span class="n">options</span><span class="o">.</span><span class="n">rtscts</span><span class="p">,</span>
</div><div id="l646" class="code_block">            <span class="n">xonxoff</span><span class="o">=</span><span class="n">options</span><span class="o">.</span><span class="n">xonxoff</span><span class="p">,</span>
</div><div id="l647" class="code_block">            <span class="n">echo</span><span class="o">=</span><span class="n">options</span><span class="o">.</span><span class="n">echo</span><span class="p">,</span>
</div><div id="l648" class="code_block">            <span class="n">convert_outgoing</span><span class="o">=</span><span class="n">convert_outgoing</span><span class="p">,</span>
</div><div id="l649" class="code_block">            <span class="n">repr_mode</span><span class="o">=</span><span class="n">options</span><span class="o">.</span><span class="n">repr_mode</span><span class="p">,</span>
</div><div id="l650" class="code_block">        <span class="p">)</span>
</div><div id="l651" class="code_block">    <span class="k">except</span> <span class="n">serial</span><span class="o">.</span><span class="n">SerialException</span><span class="p">,</span> <span class="n">e</span><span class="p">:</span>
</div><div id="l652" class="code_block">        <span class="n">sys</span><span class="o">.</span><span class="n">stderr</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="s">&quot;could not open port </span><span class="si">%r</span><span class="s">: </span><span class="si">%s</span><span class="se">\n</span><span class="s">&quot;</span> <span class="o">%</span> <span class="p">(</span><span class="n">port</span><span class="p">,</span> <span class="n">e</span><span class="p">))</span>
</div><div id="l653" class="code_block">        <span class="n">sys</span><span class="o">.</span><span class="n">exit</span><span class="p">(</span><span class="mi">1</span><span class="p">)</span>
</div><div id="l654" class="code_block">
</div><div id="l655" class="code_block">    <span class="k">if</span> <span class="ow">not</span> <span class="n">options</span><span class="o">.</span><span class="n">quiet</span><span class="p">:</span>
</div><div id="l656" class="code_block">        <span class="n">sys</span><span class="o">.</span><span class="n">stderr</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="s">&#39;--- Miniterm on </span><span class="si">%s</span><span class="s">: </span><span class="si">%d</span><span class="s">,</span><span class="si">%s</span><span class="s">,</span><span class="si">%s</span><span class="s">,</span><span class="si">%s</span><span class="s"> ---</span><span class="se">\n</span><span class="s">&#39;</span> <span class="o">%</span> <span class="p">(</span>
</div><div id="l657" class="code_block">            <span class="n">miniterm</span><span class="o">.</span><span class="n">serial</span><span class="o">.</span><span class="n">portstr</span><span class="p">,</span>
</div><div id="l658" class="code_block">            <span class="n">miniterm</span><span class="o">.</span><span class="n">serial</span><span class="o">.</span><span class="n">baudrate</span><span class="p">,</span>
</div><div id="l659" class="code_block">            <span class="n">miniterm</span><span class="o">.</span><span class="n">serial</span><span class="o">.</span><span class="n">bytesize</span><span class="p">,</span>
</div><div id="l660" class="code_block">            <span class="n">miniterm</span><span class="o">.</span><span class="n">serial</span><span class="o">.</span><span class="n">parity</span><span class="p">,</span>
</div><div id="l661" class="code_block">            <span class="n">miniterm</span><span class="o">.</span><span class="n">serial</span><span class="o">.</span><span class="n">stopbits</span><span class="p">,</span>
</div><div id="l662" class="code_block">        <span class="p">))</span>
</div><div id="l663" class="code_block">        <span class="n">sys</span><span class="o">.</span><span class="n">stderr</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="s">&#39;--- Quit: </span><span class="si">%s</span><span class="s">  |  Menu: </span><span class="si">%s</span><span class="s"> | Help: </span><span class="si">%s</span><span class="s"> followed by </span><span class="si">%s</span><span class="s"> ---</span><span class="se">\n</span><span class="s">&#39;</span> <span class="o">%</span> <span class="p">(</span>
</div><div id="l664" class="code_block">            <span class="n">key_description</span><span class="p">(</span><span class="n">EXITCHARCTER</span><span class="p">),</span>
</div><div id="l665" class="code_block">            <span class="n">key_description</span><span class="p">(</span><span class="n">MENUCHARACTER</span><span class="p">),</span>
</div><div id="l666" class="code_block">            <span class="n">key_description</span><span class="p">(</span><span class="n">MENUCHARACTER</span><span class="p">),</span>
</div><div id="l667" class="code_block">            <span class="n">key_description</span><span class="p">(</span><span class="s">&#39;</span><span class="se">\x08</span><span class="s">&#39;</span><span class="p">),</span>
</div><div id="l668" class="code_block">        <span class="p">))</span>
</div><div id="l669" class="code_block">
</div><div id="l670" class="code_block">    <span class="k">if</span> <span class="n">options</span><span class="o">.</span><span class="n">dtr_state</span> <span class="ow">is</span> <span class="ow">not</span> <span class="bp">None</span><span class="p">:</span>
</div><div id="l671" class="code_block">        <span class="k">if</span> <span class="ow">not</span> <span class="n">options</span><span class="o">.</span><span class="n">quiet</span><span class="p">:</span>
</div><div id="l672" class="code_block">            <span class="n">sys</span><span class="o">.</span><span class="n">stderr</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="s">&#39;--- forcing DTR </span><span class="si">%s</span><span class="se">\n</span><span class="s">&#39;</span> <span class="o">%</span> <span class="p">(</span><span class="n">options</span><span class="o">.</span><span class="n">dtr_state</span> <span class="ow">and</span> <span class="s">&#39;active&#39;</span> <span class="ow">or</span> <span class="s">&#39;inactive&#39;</span><span class="p">))</span>
</div><div id="l673" class="code_block">        <span class="n">miniterm</span><span class="o">.</span><span class="n">serial</span><span class="o">.</span><span class="n">setDTR</span><span class="p">(</span><span class="n">options</span><span class="o">.</span><span class="n">dtr_state</span><span class="p">)</span>
</div><div id="l674" class="code_block">        <span class="n">miniterm</span><span class="o">.</span><span class="n">dtr_state</span> <span class="o">=</span> <span class="n">options</span><span class="o">.</span><span class="n">dtr_state</span>
</div><div id="l675" class="code_block">    <span class="k">if</span> <span class="n">options</span><span class="o">.</span><span class="n">rts_state</span> <span class="ow">is</span> <span class="ow">not</span> <span class="bp">None</span><span class="p">:</span>
</div><div id="l676" class="code_block">        <span class="k">if</span> <span class="ow">not</span> <span class="n">options</span><span class="o">.</span><span class="n">quiet</span><span class="p">:</span>
</div><div id="l677" class="code_block">            <span class="n">sys</span><span class="o">.</span><span class="n">stderr</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="s">&#39;--- forcing RTS </span><span class="si">%s</span><span class="se">\n</span><span class="s">&#39;</span> <span class="o">%</span> <span class="p">(</span><span class="n">options</span><span class="o">.</span><span class="n">rts_state</span> <span class="ow">and</span> <span class="s">&#39;active&#39;</span> <span class="ow">or</span> <span class="s">&#39;inactive&#39;</span><span class="p">))</span>
</div><div id="l678" class="code_block">        <span class="n">miniterm</span><span class="o">.</span><span class="n">serial</span><span class="o">.</span><span class="n">setRTS</span><span class="p">(</span><span class="n">options</span><span class="o">.</span><span class="n">rts_state</span><span class="p">)</span>
</div><div id="l679" class="code_block">        <span class="n">miniterm</span><span class="o">.</span><span class="n">rts_state</span> <span class="o">=</span> <span class="n">options</span><span class="o">.</span><span class="n">rts_state</span>
</div><div id="l680" class="code_block">
</div><div id="l681" class="code_block">    <span class="n">console</span><span class="o">.</span><span class="n">setup</span><span class="p">()</span>
</div><div id="l682" class="code_block">    <span class="n">miniterm</span><span class="o">.</span><span class="n">start</span><span class="p">()</span>
</div><div id="l683" class="code_block">    <span class="k">try</span><span class="p">:</span>
</div><div id="l684" class="code_block">        <span class="n">miniterm</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="bp">True</span><span class="p">)</span>
</div><div id="l685" class="code_block">    <span class="k">except</span> <span class="ne">KeyboardInterrupt</span><span class="p">:</span>
</div><div id="l686" class="code_block">        <span class="k">pass</span>
</div><div id="l687" class="code_block">    <span class="k">if</span> <span class="ow">not</span> <span class="n">options</span><span class="o">.</span><span class="n">quiet</span><span class="p">:</span>
</div><div id="l688" class="code_block">        <span class="n">sys</span><span class="o">.</span><span class="n">stderr</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="s">&quot;</span><span class="se">\n</span><span class="s">--- exit ---</span><span class="se">\n</span><span class="s">&quot;</span><span class="p">)</span>
</div><div id="l689" class="code_block">    <span class="n">miniterm</span><span class="o">.</span><span class="n">join</span><span class="p">()</span>
</div><div id="l690" class="code_block">    <span class="c">#~ console.cleanup()</span>
</div><div id="l691" class="code_block">
</div><div id="l692" class="code_block"><span class="c"># - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -</span>
</div><div id="l693" class="code_block"><span class="k">if</span> <span class="n">__name__</span> <span class="o">==</span> <span class="s">&#39;__main__&#39;</span><span class="p">:</span>
</div><div id="l694" class="code_block">    <span class="n">main</span><span class="p">()</span>
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
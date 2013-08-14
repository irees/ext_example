<%inherit file="/layout" />

## This is the most general template; almost all templates inherit
## from this template, so you can specify block overrides and 
## general layout.

## There are several "blocks" defined that can be changed by child templates:
## 		css_inline
##		js_inline
##		js_ready
##		title
##		header


## Use the css_inline block to set custom CSS for this template.
<%block name="css_inline">
	## Don't forget to call the parent template's block.
	${parent.css_inline()}
	
	textarea {
		border:solid blue 2px;
	}

</%block>


## Use the js_ready block to provide JavaScript that runs after the page has loaded.
<%block name="js_ready">
	${parent.js_ready()}
	$('.e2-timeago').timeago();
</%block>


## Define a custom header.
<%block name="header">
	<div class="precontent" style="padding:0px">
		<h1 style="border-bottom:none;text-align:center">
			<a href="${EMEN2WEBROOT}/">Example Template</a>
		</h1>
		<p style="text-align:center">
			Welcome to EMEN2!
		</p>
	</div>
</%block>


## Hide the page "tabs"..
<%block name="tabs" />

## Call the next template in the chain.
${next.body()}


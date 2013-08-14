<%inherit file="/page" />

<h1>${title}</h1>

${rec.get('folder_description', '')}

<h1>Example form</h1>

<form action="" method="post">
	<textarea name="folder_description">${rec.get('folder_description', '')}</textarea><br />
	<input type="submit" value="Submit" />
</form>
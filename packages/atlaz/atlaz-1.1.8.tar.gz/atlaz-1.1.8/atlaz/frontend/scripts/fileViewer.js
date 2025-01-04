// fileViewer.js

// File viewer functionality
fetch('files.json')
    .then(response => response.json())
    .then(files => {
        const createdFilesContainer = document.getElementById('created-files');
        const filePairsContainer = document.getElementById('file-pairs');
        // Group files by base name
        const fileGroups = {};
        files.forEach(file => {
            const baseName = file.full_name.replace(/^original-|^replacing-|^created-/, '');
            if (!fileGroups[baseName]) {
                fileGroups[baseName] = {};
            }
            fileGroups[baseName][file.type] = file;
        });
        // Render created files
        for (const baseName in fileGroups) {
            const group = fileGroups[baseName];
            if (group['created'] && !group['original'] && !group['replacing']) {
                const createdFileBlock = document.createElement('div');
                createdFileBlock.classList.add('file-block');
                const fileNameDiv = document.createElement('div');
                fileNameDiv.classList.add('file-name');
                fileNameDiv.textContent = group['created'].full_name;
                const fileTypeDiv = document.createElement('div');
                fileTypeDiv.classList.add('file-type');
                fileTypeDiv.textContent = `Type: ${group['created'].type}`;
                const codeBlockDiv = document.createElement('div');
                codeBlockDiv.classList.add('code-block');
                const codePre = document.createElement('pre');
                const codeCode = document.createElement('code');
                codeCode.classList.add('language-python');
                codeCode.textContent = group['created'].content;
                codePre.appendChild(codeCode);
                codeBlockDiv.appendChild(codePre);
                createdFileBlock.appendChild(fileNameDiv);
                createdFileBlock.appendChild(fileTypeDiv);
                createdFileBlock.appendChild(codeBlockDiv);
                createdFilesContainer.appendChild(createdFileBlock);
                Prism.highlightElement(codeCode);
            }
        }
        // Render original and replacing file pairs
        for (const baseName in fileGroups) {
            const group = fileGroups[baseName];
            if (group['original'] || group['replacing']) {
                const filePairDiv = document.createElement('div');
                filePairDiv.classList.add('file-pair');
                ['original', 'replacing'].forEach(type => {
                    if (group[type]) {
                        const fileBlock = document.createElement('div');
                        fileBlock.classList.add('file-block');
                        const fileNameDiv = document.createElement('div');
                        fileNameDiv.classList.add('file-name');
                        fileNameDiv.textContent = group[type].full_name;
                        const fileTypeDiv = document.createElement('div');
                        fileTypeDiv.classList.add('file-type');
                        fileTypeDiv.textContent = `Type: ${group[type].type}`;
                        const codeBlockDiv = document.createElement('div');
                        codeBlockDiv.classList.add('code-block');
                        const codePre = document.createElement('pre');
                        const codeCode = document.createElement('code');
                        codeCode.classList.add('language-python');
                        codeCode.textContent = group[type].content;
                        codePre.appendChild(codeCode);
                        codeBlockDiv.appendChild(codePre);
                        fileBlock.appendChild(fileNameDiv);
                        fileBlock.appendChild(fileTypeDiv);
                        fileBlock.appendChild(codeBlockDiv);
                        filePairDiv.appendChild(fileBlock);
                        Prism.highlightElement(codeCode);
                    }
                });
                filePairsContainer.appendChild(filePairDiv);
            }
        }
    });
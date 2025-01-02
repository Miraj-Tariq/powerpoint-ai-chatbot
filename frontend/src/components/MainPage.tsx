import React, { useState, useEffect } from "react";
import { Box, Button, TextField } from "@mui/material";
import SearchIcon from "@mui/icons-material/Search";
import AddIcon from "@mui/icons-material/Add";
// import axios from "axios";
import Popup from "./Popup";

const MainPage: React.FC = () => {
  const [popupOpen, setPopupOpen] = useState(false);
  const [apiData, setApiData] = useState<any[]>([]);
  const [textareaValue, setTextareaValue] = useState("");

  useEffect(() => {
    Office.onReady(function (info) {
      if (info.host === Office.HostType.PowerPoint) {
        sendPresentation();

        const sendPromptButton = document.getElementById("send-prompt");
        if (sendPromptButton) {
          sendPromptButton.onclick = () => processUserInstructions(textareaValue);
        }
      }
    });
  }, [textareaValue]);

  const handleSearchSlides = async () => {
    Office.onReady((info) => {
      try {
        const dummyData = [
        { id: 1, url: "https://raw.githubusercontent.com/Miraj-Tariq/abonea-python-test-Miraj/refs/heads/master/ppt_addin_icons/test_slide.png", name: "Slide 1" },
        { id: 2, url: "https://raw.githubusercontent.com/Miraj-Tariq/abonea-python-test-Miraj/refs/heads/master/ppt_addin_icons/test_slide.png", name: "Slide 2" },
        { id: 3, url: "https://raw.githubusercontent.com/Miraj-Tariq/abonea-python-test-Miraj/refs/heads/master/ppt_addin_icons/test_slide.png", name: "Slide 3" },
        { id: 4, url: "https://raw.githubusercontent.com/Miraj-Tariq/abonea-python-test-Miraj/refs/heads/master/ppt_addin_icons/test_slide.png", name: "Slide 4" },
        { id: 5, url: "https://raw.githubusercontent.com/Miraj-Tariq/abonea-python-test-Miraj/refs/heads/master/ppt_addin_icons/test_slide.png", name: "Slide 5" },
        { id: 6, url: "https://raw.githubusercontent.com/Miraj-Tariq/abonea-python-test-Miraj/refs/heads/master/ppt_addin_icons/test_slide.png", name: "Slide 6" },
      ];

        const dialogUrl = `https://localhost:3000/dialog.html?data=${encodeURIComponent(
          JSON.stringify(dummyData)
        )}`;

        Office.context.ui.displayDialogAsync(dialogUrl, { width: 60, height: 60 }, (result) => {
          if (result.status === Office.AsyncResultStatus.Succeeded) {
            console.log("Dialog opened successfully");
          } else {
            console.error("Failed to open dialog:", result.error.message);
          }
        });
      } catch (error) {
        console.error("Error fetching search slides data", error);
      }
    });
  };

  const handleCreateSlides = () => {
    console.log("Redirect to Create Slides Screen"); // Replace with your navigation logic
  };

  const handleSend = () => {
    console.log("Textarea value:", textareaValue);
    // setTextareaValue(""); // Clear the textarea after sending
  };

  return (
    <Box display="flex" flexDirection="column" alignItems="center" padding="20px">
      <Button
        variant="outlined"
        startIcon={<SearchIcon />}
        fullWidth
        style={{ marginBottom: "10px" }}
        onClick={handleSearchSlides}
      >
        Search Slides
      </Button>
      <Button
        variant="outlined"
        startIcon={<AddIcon />}
        fullWidth
        onClick={handleCreateSlides}
      >
        Create Slides
      </Button>
      <Popup open={popupOpen} onClose={() => setPopupOpen(false)} data={apiData} />

      {/* New Section with Textarea and Button */}
      <Box mt={4} width="100%">
        <TextField
          fullWidth
          variant="outlined"
          id="user-prompt"
          placeholder="Type your message here..."
          value={textareaValue}
          onChange={(e) => setTextareaValue(e.target.value)}
          multiline
          rows={8}
        />
        <Button
          variant="contained"
          color="primary"
          fullWidth
          style={{ marginTop: "10px" }}
          id="send-prompt"
          onClick={handleSend}
        >
          SEND
        </Button>
      </Box>
    </Box>
  );
};

async function processUserInstructions(userPrompt) {
  try {
    let shapesInfo = [];
    let slidesInfo = [];
    let insertOptions = {};

    await PowerPoint.run(async (context) => {
      // Current Slide Info
      context.presentation.load("slides");
      await context.sync();
      const allSlidesList = {};
      context.presentation.slides.load("items");
      await context.sync();
      let allSlideItems = context.presentation.slides.items;
      allSlideItems.map((slide, index) => {
        allSlidesList[slide.id] = index;
      });

      const selectedSlides = context.presentation.getSelectedSlides();
      const firstSelectedSlide = selectedSlides.getItemAt(0);

      firstSelectedSlide.load("id");
      selectedSlides.load("items");
      await context.sync();

      insertOptions = {
        formatting: PowerPoint.InsertSlideFormatting.useDestinationTheme,
        targetSlideId: firstSelectedSlide.id,
      };

      console.log(`Total number of slides: ${selectedSlides.items.length}`);

      for (const slide of selectedSlides.items) {
        slide.load("id");
      }
      await context.sync();

      for (const slide of selectedSlides.items) {
        const slideInfo = {
          id: slide.id,
          index: allSlidesList[slide.id],
        };

        slidesInfo.push(slideInfo);
      }

      const selectedShapes = context.presentation.getSelectedShapes();
      selectedShapes.load("items");
      await context.sync();

      console.log(`Total number of shapes: ${selectedShapes.items.length}`);

      for (const shape of selectedShapes.items) {
        shape.load(["name", "type"]);
      }
      await context.sync();

      for (const shape of selectedShapes.items) {
        const shapeInfo = {
          name: shape.name,
          type: shape.type,
        };

        shapesInfo.push(shapeInfo);
      }
    });

    // const userPrompt = document.getElementById("user-prompt").value;
    // const userPrompt = textareaValue;
    console.log(`User prompt is ${userPrompt}`);
    let responseData = {};
    fetch("http://localhost:8000/process", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        prompt: userPrompt,
        slidesInfo: slidesInfo,
        shapesInfo: shapesInfo,
      }),
    })
      .then((response) => response.json())
      .then((data) => {
        console.log("Success:", data);
        if (data["base64_encoded_ppt"]) {
          PowerPoint.run(async (context) => {
            context.presentation.insertSlidesFromBase64(
              data["base64_encoded_ppt"],
              insertOptions
            );
            await context.sync();

            const slides = context.presentation.slides;
            slides.load("items");
            await context.sync();

            const deleted_slide = slides.items[data.input_data.slidesInfo[0].index];
            deleted_slide.delete();
            await context.sync();
          }).catch((error) => {
            console.error("Error during PowerPoint.run for slide insertion: ", error);
          });
        } else {
          console.error("Error: Base64 encoded PowerPoint data is missing.");
        }
      })
      .catch((error) => {
        console.error("Error:", error);
      });

    await sendPresentation();
  } catch (error) {
    console.error("Error in sending prompt backend: ", error);
  }
}

async function computeSHA256(arrayBuffer) {
  const hashBuffer = await crypto.subtle.digest("SHA-256", arrayBuffer);
  const hashArray = Array.from(new Uint8Array(hashBuffer));
  const hashHex = hashArray.map((b) => b.toString(16).padStart(2, "0")).join("");
  return hashHex;
}

async function sendPresentation() {
  try {
    await PowerPoint.run(async (context) => {
      const document = Office.context.document;
      await context.sync();

      document.getFileAsync(
        Office.FileType.Compressed,
        { sliceSize: 65536 },
        async function (fileResult) {
          if (fileResult.status === Office.AsyncResultStatus.Succeeded) {
            const file = fileResult.value;
            const sliceCount = file.sliceCount;
            let chunks = [];

            for (let i = 0; i < sliceCount; i++) {
              await new Promise((resolve, reject) => {
                file.getSliceAsync(i, function (sliceResult) {
                  if (sliceResult.status === Office.AsyncResultStatus.Succeeded) {
                    const byteArray = new Uint8Array(sliceResult.value.data);
                    chunks.push(byteArray);
                    resolve();
                  } else {
                    console.error("Error in getting file slice: ", sliceResult.error.message);
                    reject(sliceResult.error);
                  }
                });
              });
            }

            file.closeAsync();

            const totalLength = chunks.reduce((acc, curr) => acc + curr.length, 0);
            const combined = new Uint8Array(totalLength);
            let offset = 0;
            for (let chunk of chunks) {
              combined.set(chunk, offset);
              offset += chunk.length;
            }

            const checksum = await computeSHA256(combined.buffer);
            console.log("SHA256 Checksum: ", checksum);

            const blob = new Blob([combined], {
              type: "application/vnd.openxmlformats-officedocument.presentationml.presentation",
            });

            const formData = new FormData();
            formData.append("presentation", blob, "presentation.pptx");
            formData.append("checksum", checksum);

            const response = await fetch("http://localhost:8000/upload", {
              method: "POST",
              body: formData,
            });

            if (!response.ok) {
              const errorData = await response.text();
              throw new Error(`Server error: ${response.status} - ${errorData}`);
            }

            const responseData = await response.json();
            console.log("Backend Response: ", responseData);
          } else {
            console.error("Error in getting presentation file: ", fileResult.error.message);
          }
        }
      );
    });
  } catch (error) {
    console.error("Error in sending presentation: ", error);
  }
}

export default MainPage;

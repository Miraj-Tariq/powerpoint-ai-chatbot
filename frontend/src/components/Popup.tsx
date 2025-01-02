import React, { useState, useEffect } from "react";
import {
  Dialog,
  DialogTitle,
  DialogContent,
  DialogActions,
  Button,
  TextField,
  Tabs,
  Tab,
  Grid,
  Checkbox,
  Typography,
  Box,
} from "@mui/material";
// import axios from "axios";

interface PopupProps {
  open: boolean;
  onClose: () => void;
}

const Popup: React.FC<PopupProps> = ({ open, onClose }) => {
  const [searchText, setSearchText] = useState<string>("");
  const [activeTab, setActiveTab] = useState<number>(0); // Tabs: 0 - Recent Slides, 1 - Most Common Files, etc.
  const [images, setImages] = useState<any[]>([]); // Image data from API
  const [currentPage, setCurrentPage] = useState<number>(1); // For pagination
  const [selectedSlides, setSelectedSlides] = useState<Set<number>>(new Set());

  const handleSearch = async () => {
    // Call API with search text
    // const response = await axios.post("http://localhost:8787/search_slides/", {
    //   search: searchText,
    //   page: currentPage,
    // });
    // Replace API response with dummy data
        const dummyData = [
         "https://raw.githubusercontent.com/Miraj-Tariq/abonea-python-test-Miraj/refs/heads/master/ppt_addin_icons/test_slide.png",
         "https://raw.githubusercontent.com/Miraj-Tariq/abonea-python-test-Miraj/refs/heads/master/ppt_addin_icons/test_slide.png",
         "https://raw.githubusercontent.com/Miraj-Tariq/abonea-python-test-Miraj/refs/heads/master/ppt_addin_icons/test_slide.png",
         "https://raw.githubusercontent.com/Miraj-Tariq/abonea-python-test-Miraj/refs/heads/master/ppt_addin_icons/test_slide.png",
         "https://raw.githubusercontent.com/Miraj-Tariq/abonea-python-test-Miraj/refs/heads/master/ppt_addin_icons/test_slide.png",
         "https://raw.githubusercontent.com/Miraj-Tariq/abonea-python-test-Miraj/refs/heads/master/ppt_addin_icons/test_slide.png",
        ];
    setImages(dummyData); // Assuming API returns an array of images
  };

  const handleTabChange = (_event: React.SyntheticEvent, newValue: number) => {
    setActiveTab(newValue);
    setImages([]); // Reset images when switching tabs
    setCurrentPage(1); // Reset to first page
    // Call API here if each tab corresponds to a different API
  };

  const handleImageSelect = (id: number) => {
    const newSelectedSlides = new Set(selectedSlides);
    if (newSelectedSlides.has(id)) {
      newSelectedSlides.delete(id);
    } else {
      newSelectedSlides.add(id);
    }
    setSelectedSlides(newSelectedSlides);
  };

  const handleAddToDeck = async () => {
    // Call API with selected slides
    // const response = await axios.post("http://localhost:8787/add_to_deck/", {
    //   selectedSlides: Array.from(selectedSlides),
    // });
    console.log("Added Slides to Deck");
    onClose(); // Close popup after API call
  };

  useEffect(() => {
    // Initial API call when popup opens
    if (open) {
      handleSearch();
    }
  }, [open, currentPage]);

  return (
    <Dialog open={open} onClose={onClose} fullWidth maxWidth="lg">
      <DialogTitle>ColumnsRows</DialogTitle>
      <DialogContent>
        {/* Search Bar */}
        <Box marginBottom={2}>
          <TextField
            fullWidth
            variant="outlined"
            placeholder="Search for slides by typing down the content or the visuals"
            value={searchText}
            onChange={(e) => setSearchText(e.target.value)}
            onKeyDown={(e) => {
              if (e.key === "Enter") handleSearch();
            }}
          />
        </Box>

        {/* Tabs */}
        <Tabs
          value={activeTab}
          onChange={handleTabChange}
          variant="fullWidth"
          textColor="primary"
          indicatorColor="primary"
        >
          <Tab label="Recent slides" />
          <Tab label="Most common files" />
          <Tab label="Your favorite slides" />
          <Tab label="Selected slides" />
        </Tabs>

        {/* Images Grid */}
        <Grid container spacing={2} marginTop={2}>
          {images.map((image, index) => (
            <Grid item xs={4} key={index}>
              <Box
                position="relative"
                border="1px solid #ddd"
                borderRadius="8px"
                padding="8px"
                textAlign="center"
              >
                <img
                  src={image.url} // Replace with actual image property
                  alt={`Slide ${index + 1}`}
                  style={{
                    maxWidth: "100%",
                    maxHeight: "150px",
                    objectFit: "cover",
                    marginBottom: "8px",
                  }}
                />
                <Typography variant="body2">{image.name}</Typography>
                <Checkbox
                  checked={selectedSlides.has(image.id)} // Assuming `id` is the unique identifier
                  onChange={() => handleImageSelect(image.id)}
                  style={{ position: "absolute", top: 8, left: 8 }}
                />
              </Box>
            </Grid>
          ))}
        </Grid>

        {/* Pagination */}
        <Box display="flex" justifyContent="center" marginTop={2}>
          <Button
            onClick={() => setCurrentPage((prev) => Math.max(prev - 1, 1))}
            disabled={currentPage === 1}
          >
            Previous
          </Button>
          <Typography variant="body2" marginX={2}>
            Page {currentPage}
          </Typography>
          <Button onClick={() => setCurrentPage((prev) => prev + 1)}>
            Next
          </Button>
        </Box>
      </DialogContent>

      {/* Add to Deck Button */}
      <DialogActions>
        <Button
          variant="contained"
          color="primary"
          onClick={handleAddToDeck}
          disabled={selectedSlides.size === 0}
        >
          Add to Deck
        </Button>
      </DialogActions>
    </Dialog>
  );
};

export default Popup;

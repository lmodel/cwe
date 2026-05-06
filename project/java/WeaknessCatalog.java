package None;

/* metamodel_version: 1.7.0 */
/* version: 7.3 */
import java.util.List;
import lombok.*;

/**
  Top-level container for a CWE catalog snapshot (Weakness_Catalog in XSD). Holds weakness entries, categories, views, external references, and NVD weakness observations.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class WeaknessCatalog  {

  private String name;
  private String version;
  private LocalDate date;
  private List<Weakness> weaknesses;
  private List<Category> categories;
  private List<View> views;
  private List<ExternalReference> externalReferences;
  private List<NVDWeaknessObservation> observations;

}